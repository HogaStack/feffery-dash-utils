import json
import logging
from flask import request
from typing import Callable, Optional, Union


__all__ = ['Translator']


logger = logging.getLogger('i18n')


class Translator:
    """实现文案内容的快捷国际化相关操作"""

    def __init__(
        self,
        translations: Union[str, list],
        translations_encoding: str = 'utf-8',
        root_locale: Union[str, None] = None,
        cookie_name: str = 'dash-i18n',
        get_current_locale: Optional[Callable] = None,
        force_check_content_translator: bool = True,
    ) -> None:
        """
        初始化 Translator 实例

        Args:
            translations (Union[str, list])：单个本地化配置文件路径，或多个本地化配置文件路径列表
            translations_encoding (str)：本地化配置文件编码 Defaults to 'utf-8'
            root_locale (Union[str, None], optional)：手动设置的根语言环境类型 Defaults to None
            cookie_name (str)：存储当前语言环境类型的 cookie 名称 Defaults to 'dash-i18n'
            get_current_locale (Optional[Callable]): 自定义函数或方法，返回值表示当前语言环境类型
            force_check_content_translator (bool, optional): 是否针对文案翻译内容存在性进行检查
        Returns:
            None
        """

        # 重建国际化配置参数，并获取根语种
        root_locale_from_json = self.rebuild_transilations(
            translations=translations,
            translations_encoding=translations_encoding,
        )
        self.root_locale = root_locale or root_locale_from_json
        self.cookie_name = cookie_name
        if get_current_locale is None:
            self.get_current_locale = lambda: (
                request.cookies.get(self.cookie_name) or self.root_locale
            )
        else:
            self.get_current_locale = get_current_locale
        self.forced_check_content_translator = force_check_content_translator

    def t(
        self,
        input_content: str,
        source_locale: Union[str, None] = None,
        locale_topic: str = '_default',
    ) -> str:
        """
        文案内容国际化转换

        Args:
            input_content (str): 转换前文案内容
            source_locale (Union[str, None], optional): 手动控制源语种 Defaults to None
            locale_topic (str, optional): 手动控制目标语种主题 Defaults to '_default'

        Returns:
            str: 转换结果
        """

        # 确定本次翻译提取的源语种
        source_locale = source_locale or self.root_locale

        current_locale = self.get_current_locale()

        assert current_locale is not None, (
            '未从cookie中检测到当前语种 %s' % current_locale
        )
        assert current_locale in self.available_locales, (
            '检测到的当前语种不在配置信息中 %s' % current_locale
        )
        assert locale_topic in self.available_topics, (
            '检测到的目标语种主题不在配置信息中 %s' % locale_topic
        )

        # 尝试从已加载的配置信息中的对应主题提取目标文案语种
        if source_locale != current_locale:
            assert source_locale in self.translations[locale_topic], (
                '%s 未从 %s 主题的配置信息中检测到源文案语种'
                % (input_content, locale_topic)
            )

            match_transitions = self.translations[locale_topic][
                source_locale
            ].get(input_content)

            if self.forced_check_content_translator:
                assert match_transitions is not None, (
                    '%s 未从配置信息中检测到目标文案语种' % input_content
                )
                assert match_transitions.get(current_locale) is not None, (
                    '%s 未从配置信息中检测到目标文案语种的翻译内容'
                    % input_content
                )
                return match_transitions[current_locale]
            else:
                if (
                    match_transitions is not None
                    and match_transitions.get(current_locale) is not None
                ):
                    return match_transitions[current_locale]
                else:
                    logger.warning(
                        '%s 未检测到目标文案语种的翻译内容，将使用默认文案内容'
                        % input_content
                    )
                    return input_content
        return input_content

    def rebuild_transilations(
        self,
        translations: Union[str, list],
        translations_encoding: str = 'utf-8',
    ) -> str:
        """
        基于传入的本地国际化配置文件重置国际化配置参数

        Args:
            translations (Union[str, list])：单个本地化配置文件路径，或多个本地化配置文件路径列表
            translations_encoding (str, optional): 本地化配置文件编码 Defaults to 'utf-8'

        Returns:
            str: 解析结果中的根语种
        """

        if isinstance(translations, str):
            translations = [translations]

        assert len(translations) > 0, '无效的本地化配置文件路径'

        raw_root_locales = []
        raw_translations = {}
        for translation in translations:
            # 读取当前对应的目标本地国际化配置文件
            with open(
                translation,
                'r',
                encoding=translations_encoding,
            ) as f:
                raw_translation = json.load(f)

            assert raw_translation.get('root_locale'), (
                '配置文件： %s root_locale 无效' % translation
            )

            raw_root_locales.append(raw_translation['root_locale'])

            assert len(set(raw_root_locales)) == 1, (
                '构建到配置文件 %s 时检测到多个根语种' % translation
            )

            # 根据当前配置文件的topic主题，构建或增长对应的原始文案映射字典
            if raw_translation.get('topic'):
                # 初始化或覆盖当前topic
                raw_translations[raw_translation['topic']] = raw_translation
            else:
                # 初始化或覆盖默认topic
                raw_translations['_default'] = raw_translation

        # 针对不同主题，构建内部独立的的文案映射字典
        self.translations = {}
        for (
            topic,
            topic_translations,
        ) in raw_translations.items():
            # 初始化当前主题对应的文案映射字典
            self.translations[topic] = {
                topic_translations['root_locale']: topic_translations[
                    'contents'
                ]
            }

            # 补充生成其他语种文案映射字典
            self.available_locales = []
            for (
                root_content,
                root_content_translations,
            ) in topic_translations['contents'].items():
                for (
                    locale,
                    content,
                ) in root_content_translations.items():
                    if locale not in self.translations[topic]:
                        self.translations[topic][locale] = {}
                    if content not in self.translations[topic][locale]:
                        self.translations[topic][locale][content] = {}
                    self.translations[topic][locale][content].update(
                        {
                            raw_translations[topic][
                                'root_locale'
                            ]: root_content,
                            **{
                                key: value
                                for key, value in root_content_translations.items()
                                if key != locale
                            },
                        }
                    )
                    self.available_locales.append(locale)

        # 更新当前可用主题列表
        self.available_topics = list(self.translations.keys())
        # 补充根语种
        self.available_locales.append(raw_root_locales[0])
        # 更新当前可用语种列表
        self.available_locales = list(set(self.available_locales))

        # 返回当前根语种
        return raw_root_locales[0]
