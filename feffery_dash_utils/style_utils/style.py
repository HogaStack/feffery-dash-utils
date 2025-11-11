import inspect
from cssutils import parseString
from typing import Union

def style(
    rawCSS: Union[str, None] = None,
    alignContent=None,
    alignItems=None,
    alignSelf=None,
    all=None,
    animation=None,
    animationDelay=None,
    animationDirection=None,
    animationDuration=None,
    animationFillMode=None,
    animationIterationCount=None,
    animationName=None,
    animationPlayState=None,
    animationTimingFunction=None,
    backfaceVisibility=None,
    background=None,
    backgroundAttachment=None,
    backgroundBlendMode=None,
    backgroundClip=None,
    backgroundColor=None,
    backgroundImage=None,
    backgroundOrigin=None,
    backgroundPosition=None,
    backgroundRepeat=None,
    backgroundSize=None,
    border=None,
    borderBottom=None,
    borderBottomColor=None,
    borderBottomLeftRadius=None,
    borderBottomRightRadius=None,
    borderBottomStyle=None,
    borderBottomWidth=None,
    borderCollapse=None,
    borderColor=None,
    borderImage=None,
    borderImageOutset=None,
    borderImageRepeat=None,
    borderImageSlice=None,
    borderImageSource=None,
    borderImageWidth=None,
    borderLeft=None,
    borderLeftColor=None,
    borderLeftStyle=None,
    borderLeftWidth=None,
    borderRadius=None,
    borderRight=None,
    borderRightColor=None,
    borderRightStyle=None,
    borderRightWidth=None,
    borderSpacing=None,
    borderStyle=None,
    borderTop=None,
    borderTopColor=None,
    borderTopLeftRadius=None,
    borderTopRightRadius=None,
    borderTopStyle=None,
    borderTopWidth=None,
    borderWidth=None,
    bottom=None,
    boxDecorationBreak=None,
    boxShadow=None,
    boxSizing=None,
    breakAfter=None,
    breakBefore=None,
    breakInside=None,
    captionSide=None,
    caretColor=None,
    clear=None,
    clip=None,
    clipPath=None,
    color=None,
    columnCount=None,
    columnFill=None,
    columnGap=None,
    columnRule=None,
    columnRuleColor=None,
    columnRuleStyle=None,
    columnRuleWidth=None,
    columnSpan=None,
    columnWidth=None,
    columns=None,
    content=None,
    counterIncrement=None,
    counterReset=None,
    cursor=None,
    direction=None,
    display=None,
    emptyCells=None,
    filter=None,
    flex=None,
    flexBasis=None,
    flexDirection=None,
    flexFlow=None,
    flexGrow=None,
    flexShrink=None,
    flexWrap=None,
    float=None,
    font=None,
    fontFamily=None,
    fontFeatureSettings=None,
    fontKerning=None,
    fontLanguageOverride=None,
    fontSize=None,
    fontSizeAdjust=None,
    fontStretch=None,
    fontStyle=None,
    fontSynthesis=None,
    fontVariant=None,
    fontVariantAlternates=None,
    fontVariantCaps=None,
    fontVariantEastAsian=None,
    fontVariantLigatures=None,
    fontVariantNumeric=None,
    fontVariantPosition=None,
    fontWeight=None,
    grid=None,
    gridArea=None,
    gridAutoColumns=None,
    gridAutoFlow=None,
    gridAutoRows=None,
    gridColumn=None,
    gridColumnEnd=None,
    gridColumnGap=None,
    gridColumnStart=None,
    gridGap=None,
    gridRow=None,
    gridRowEnd=None,
    gridRowGap=None,
    gridRowStart=None,
    gridTemplate=None,
    gridTemplateAreas=None,
    gridTemplateColumns=None,
    gridTemplateRows=None,
    hangingPunctuation=None,
    height=None,
    hyphens=None,
    imageRendering=None,
    isolation=None,
    justifyContent=None,
    justifyItems=None,
    justifySelf=None,
    left=None,
    letterSpacing=None,
    lineBreak=None,
    lineHeight=None,
    listStyle=None,
    listStyleImage=None,
    listStylePosition=None,
    listStyleType=None,
    margin=None,
    marginBottom=None,
    marginLeft=None,
    marginRight=None,
    marginTop=None,
    mask=None,
    maskType=None,
    maxHeight=None,
    maxWidth=None,
    minHeight=None,
    minWidth=None,
    mixBlendMode=None,
    objectFit=None,
    objectPosition=None,
    opacity=None,
    order=None,
    orphans=None,
    outline=None,
    outlineColor=None,
    outlineOffset=None,
    outlineStyle=None,
    outlineWidth=None,
    overflowWrap=None,
    overflowX=None,
    overflowY=None,
    padding=None,
    paddingBottom=None,
    paddingLeft=None,
    paddingRight=None,
    paddingTop=None,
    pageBreakAfter=None,
    pageBreakBefore=None,
    pageBreakInside=None,
    perspective=None,
    perspectiveOrigin=None,
    pointerEvents=None,
    position=None,
    quotes=None,
    resize=None,
    right=None,
    scrollBehavior=None,
    tabSize=None,
    tableLayout=None,
    textAlign=None,
    textAlignLast=None,
    textCombineUpright=None,
    textDecoration=None,
    textDecorationColor=None,
    textDecorationLine=None,
    textDecorationStyle=None,
    textIndent=None,
    textJustify=None,
    textOrientation=None,
    textOverflow=None,
    textShadow=None,
    textTransform=None,
    textUnderlinePosition=None,
    top=None,
    transform=None,
    transformOrigin=None,
    transformStyle=None,
    transition=None,
    transitionDelay=None,
    transitionDuration=None,
    transitionProperty=None,
    transitionTimingFunction=None,
    unicodeBidi=None,
    userSelect=None,
    verticalAlign=None,
    visibility=None,
    whiteSpace=None,
    widows=None,
    width=None,
    wordBreak=None,
    wordSpacing=None,
    wordWrap=None,
    writingMode=None,
    zIndex=None,
    **kwargs
) -> dict:
    """
    Args:
        - rawCSS: 接受原始CSS字符串，用于自动解析相应的样式属性键值对。  Accepts the original CSS string to automatically parse the corresponding style property key-value pairs
        - alignContent: 规定弹性容器内的行之间的对齐方式，当项目不使用所有可用空间时。  Specifies the alignment between the lines inside a flexible container when the items do not use all available space
        - alignItems: 规定弹性容器内项目的对齐方式。  Specifies the alignment for items inside a flexible container
        - alignSelf: 规定弹性容器内所选项目的对齐方式。  Specifies the alignment for selected items inside a flexible container
        - all: 重置所有属性（除了 unicode-bidi 和 direction）。  Resets all properties (except unicode-bidi and direction)
        - animation: 所有 animation-* 属性的简写属性。  A shorthand property for all the animation-* properties
        - animationDelay: 规定开始动画的延迟。  Specifies a delay for the start of an animation
        - animationDirection: 规定动画是向前播放、向后播放还是交替播放。  Specifies whether an animation should be played forwards, backwards or in alternate cycles
        - animationDuration: 规定动画完成一个周期应花费的时间。  Specifies how long an animation should take to complete one cycle
        - animationFillMode: 规定元素在不播放动画时（在开始之前、结束之后、或同时）的样式。  Specifies a style for the element when the animation is not playing (before it starts, after it ends, or both)
        - animationIterationCount: 规定动画的播放次数。  Specifies the number of times an animation should be played
        - animationName: 规定 @keyframes 动画的名称。  Specifies a name for the @keyframes animation
        - animationPlayState: 规定动画是播放还是暂停。  Specifies whether the animation is running or paused
        - animationTimingFunction: 规定动画的速度曲线。  Specifies the speed curve of an animation
        - backfaceVisibility: 定义当面对用户时元素的背面是否应可见。  Defines whether or not the back face of an element should be visible when facing the user
        - background: 所有 background-* 属性的简写属性。  A shorthand property for all the background-* properties
        - backgroundAttachment: 设置背景图像是与页面的其余部分一起滚动还是固定的。  Sets whether a background image scrolls with the rest of the page, or is fixed
        - backgroundBlendMode: 规定每个背景图层（颜色/图像）的混合模式。  Specifies the blending mode of each background layer (color/image)
        - backgroundClip: 定义背景（颜色或图像）应在元素内延伸的距离。  Defines how far the background (color or image) should extend within an element
        - backgroundColor: 规定元素的背景色。  Specifies the background color of an element
        - backgroundImage: 规定元素的一幅或多幅背景图像。  Specifies one or more background images for an element
        - backgroundOrigin: 规定背景图像的初始位置。  Specifies the origin position of a background image
        - backgroundPosition: 规定背景图像的位置。  Specifies the position of a background image
        - backgroundRepeat: 设置是否以及如何重复背景图像。  Sets if/how a background image will be repeated
        - backgroundSize: 规定背景图像的尺寸。  Specifies the size of the background images
        - border: border-width、border-style 以及 border-color 的简写属性。  A shorthand property for border-width, border-style and border-color
        - borderBottom: border-bottom-width、border-bottom-style 以及 border-bottom-color 的简写属性。  A shorthand property for border-bottom-width, border-bottom-style and border-bottom-color
        - borderBottomColor: 设置下边框的颜色。  Sets the color of the bottom border
        - borderBottomLeftRadius: 定义左下角的边框圆角。  Defines the radius of the border of the bottom-left corner
        - borderBottomRightRadius: 定义右下角的边框圆角。  Defines the radius of the border of the bottom-right corner
        - borderBottomStyle: 设置下边框的样式。  Sets the style of the bottom border
        - borderBottomWidth: 设置下边框的宽度。  Sets the width of the bottom border
        - borderCollapse: 设置表格边框是折叠为单一边框还是分开的。  Sets whether table borders should collapse into a single border or be separated
        - borderColor: 设置四条边框的颜色。  Sets the color of the four borders
        - borderImage: border-image-* 属性的简写属性。  A shorthand property for all the border-image-* properties
        - borderImageOutset: 规定边框图像区域超出边框的量。  Specifies the amount by which the border image area extends beyond the border box
        - borderImageRepeat: 规定边框图像应重复、圆角、还是拉伸。  Specifies whether the border image should be repeated, rounded or stretched
        - borderImageSlice: 规定如何裁切边框图像。  Specifies how to slice the border image
        - borderImageSource: 规定用作边框的图像的路径。  Specifies the path to the image to be used as a border
        - borderImageWidth: 规定边框图像的宽度。  Specifies the width of the border image
        - borderLeft: 所有 border-left-* 属性的简写属性。  A shorthand property for all the border-left-* properties
        - borderLeftColor: 设置左边框的颜色。  Sets the color of the left border
        - borderLeftStyle: 设置左边框的样式。  Sets the style of the left border
        - borderLeftWidth: 设置左边框的宽度。  Sets the width of the left border
        - borderRadius: 四个 border-*-radius 属性的简写属性。  A shorthand property for the four border-*-radius properties
        - borderRight: 所有 border-right-* 属性的简写属性。  A shorthand property for all the border-right-* properties
        - borderRightColor: 设置右边框的颜色。  Sets the color of the right border
        - borderRightStyle: 设置右边框的样式。  Sets the style of the right border
        - borderRightWidth: 设置右边框的宽度。  Sets the width of the right border
        - borderSpacing: 设置相邻单元格边框之间的距离。  Sets the distance between the borders of adjacent cells
        - borderStyle: 设置四条边框的样式。  Sets the style of the four borders
        - borderTop: border-top-width、border-top-style 以及 border-top-color 的简写属性。  A shorthand property for border-top-width, border-top-style and border-top-color
        - borderTopColor: 设置上边框的颜色。  Sets the color of the top border
        - borderTopLeftRadius: 定义左上角的边框圆角。  Defines the radius of the border of the top-left corner
        - borderTopRightRadius: 定义右上角的边框圆角。  Defines the radius of the border of the top-right corner
        - borderTopStyle: 设置上边框的样式。  Sets the style of the top border
        - borderTopWidth: 设置上边框的宽度。  Sets the width of the top border
        - borderWidth: 设置四条边框的宽度。  Sets the width of the four borders
        - bottom: 设置元素相对于其父元素底部的位置。  Sets the elements position, from the bottom of its parent element
        - boxDecorationBreak: 设置元素在分页符处的背景和边框的行为，或对于行内元素在换行符处的行为。  Sets the behavior of the background and border of an element at page-break, or, for in-line elements, at line-break.
        - boxShadow: 将一个或多个阴影附加到元素。  Attaches one or more shadows to an element
        - boxSizing: 定义元素的宽度和高度的计算方式：它们是否应包含内边距和边框。  Defines how the width and height of an element are calculated: should they include padding and borders, or not
        - breakAfter: 规定指定元素之后是否应出现 page-、column- 或 region-break。  Specifies whether or not a page-, column-, or region-break should occur after the specified element
        - breakBefore: 规定指定元素之前是否应出现 page-、column- 或 region-break。  Specifies whether or not a page-, column-, or region-break should occur before the specified element
        - breakInside: 规定指定元素内部是否应出现 page-、column- 或 region-break。  Specifies whether or not a page-, column-, or region-break should occur inside the specified element
        - captionSide: 规定表格标题的放置方式。  Specifies the placement of a table caption
        - caretColor: 规定光标在 input、textarea 或任何可编辑元素中的颜色。  Specifies the color of the cursor (caret) in inputs, textareas, or any element that is editable
        - clear: 规定不允许在元素的哪一侧浮动元素  Specifies what should happen with the element that is next to a floating element
        - clip: 剪裁绝对定位的元素。  Clips an absolutely positioned element
        - clipPath: 将元素裁剪为基本形状或 SVG 源。  Clips an element to a basic shape or to an SVG source
        - color: 设置文本的颜色。  Sets the color of text
        - columnCount: 规定元素应分为的列数。  Specifies the number of columns an element should be divided into
        - columnFill: 指定如何填充列（是否 balanced）。  Specifies how to fill columns, balanced or not
        - columnGap: 规定列间隙。  Specifies the gap between the columns
        - columnRule: 所有 column-rule-* 属性的简写属性。  A shorthand property for all the column-rule-* properties
        - columnRuleColor: 规定列之间规则的颜色。  Specifies the color of the rule between columns
        - columnRuleStyle: 规定列之间的规则样式。  Specifies the style of the rule between columns
        - columnRuleWidth: 规定列之间的规则宽度。  Specifies the width of the rule between columns
        - columnSpan: 规定元素应该跨越多少列。  Specifies how many columns an element should span across
        - columnWidth: 规定列宽度。  Specifies the column width
        - columns: column-width 和 column-count 的简写属性。  A shorthand property for column-width and column-count
        - content: 与 :before 和 :after 伪元素一起使用，来插入生成的内容。  Used with the :before and :after pseudo-elements, to insert generated content
        - counterIncrement: 增加或减少一个或多个 CSS 计数器的值。  Increases or decreases the value of one or more CSS counters
        - counterReset: 创建或重置一个或多个 CSS 计数器。  Creates or resets one or more CSS counters
        - cursor: 规定当指向元素时要显示的鼠标光标。  Specifies the mouse cursor to be displayed when pointing over an element
        - direction: 规定文本方向/书写方向。  Specifies the text direction/writing direction
        - display: 规定如何显示某个 HTML 元素。  Specifies how a certain HTML element should be displayed
        - emptyCells: 规定是否在表格中的空白单元格上显示边框和背景。  Specifies whether or not to display borders and background on empty cells in a table
        - filter: 定义元素显示之前的效果（例如，模糊或颜色偏移）。  Defines effects (e.g. blurring or color shifting) on an element before the element is displayed
        - flex: flex-grow、flex-shrink 以及 flex-basis 的简写属性。  A shorthand property for the flex-grow, flex-shrink, and the flex-basis properties
        - flexBasis: 规定弹性项目的初始长度。  Specifies the initial length of a flexible item
        - flexDirection: 规定弹性项目的方向。  Specifies the direction of the flexible items
        - flexFlow: flex-direction 和 flex-wrap 的简写属性。  A shorthand property for the flex-direction and the flex-wrap properties
        - flexGrow: 规定项目相对于其余项目的增量。  Specifies how much the item will grow relative to the rest
        - flexShrink: 规定项目相对于其余项目的减量。  Specifies how the item will shrink relative to the rest
        - flexWrap: 规定弹性项目是否应该换行。  Specifies whether the flexible items should wrap or not
        - float: 规定是否应该对盒（box）进行浮动。  Specifies whether an element should float to the left, right, or not at all
        - font: font-style、font-variant、font-weight、font-size/line-height 以及 font-family 的简写属性。  A shorthand property for the font-style, font-variant, font-weight, font-size/line-height, and the font-family properties
        - fontFamily: 规定文本的字体族（字体系列）。  Specifies the font family for text
        - fontFeatureSettings: 允许控制 OpenType 字体中的高级印刷特性。  Allows control over advanced typographic features in OpenType fonts
        - fontKerning: 控制字距调整信息的使用（字母间距）。  Controls the usage of the kerning information (how letters are spaced)
        - fontLanguageOverride: 控制特定语言的字形在字体的使用。  Controls the usage of language-specific glyphs in a typeface
        - fontSize: 规定文本的字体大小。  Specifies the font size of text
        - fontSizeAdjust: 保持发生字体回退时的可读性。  Preserves the readability of text when font fallback occurs
        - fontStretch: 从字体系列中选择一个普通的、压缩的或扩展的字体。  Selects a normal, condensed, or expanded face from a font family
        - fontStyle: 规定文本的字体样式。  Specifies the font style for text
        - fontSynthesis: 控制哪些缺失的字体（粗体或斜体）可以由浏览器合成。  Controls which missing typefaces (bold or italic) may be synthesized by the browser
        - fontVariant: 规定是否应该以小型大写字体显示文本。  Specifies whether or not a text should be displayed in a small-caps font
        - fontVariantAlternates: 控制与 @font-feature-values 中定义的备用名称关联的备用字形的使用。  Controls the usage of alternate glyphs associated to alternative names defined in @font-feature-values
        - fontVariantCaps: 控制大写字母的备用字形的使用。  Controls the usage of alternate glyphs for capital letters
        - fontVariantEastAsian: 控制东亚文字（例如中文和日语）的备用字形的使用。  Controls the usage of alternate glyphs for East Asian scripts (e.g Japanese and Chinese)
        - fontVariantLigatures: 控制在适用于元素的文本内容中使用哪些连字和上下文形式。  Controls which ligatures and contextual forms are used in textual content of the elements it applies to
        - fontVariantNumeric: 控制数字、分数和序号标记的备用字形的使用。  Controls the usage of alternate glyphs for numbers, fractions, and ordinal markers
        - fontVariantPosition: 控制较小字体的替代字形的使用，这些字形相对于字体基线定位为上标或下标。  Controls the usage of alternate glyphs of smaller size positioned as superscript or subscript regarding the baseline of the font
        - fontWeight: 规定字体的粗细。  Specifies the weight of a font
        - grid: grid-template-rows、grid-template-columns、grid-template-areas、grid-auto-rows、grid-auto-columns 以及 grid-auto-flow 属性的简写属性。  A shorthand property for the grid-template-rows, grid-template-columns, grid-template-areas, grid-auto-rows, grid-auto-columns, and the grid-auto-flow properties
        - gridArea: 即可规定网格项的名称，也可以是 grid-row-start、grid-column-start、grid-row-end 以及 grid-column-end 属性的简写属性。  Either specifies a name for the grid item, or this property is a shorthand property for the grid-row-start, grid-column-start, grid-row-end, and grid-column-end properties
        - gridAutoColumns: 规定默认的列尺寸。  Specifies a default column size
        - gridAutoFlow: 规定如何在网格中插入自动放置的项目。  Specifies how auto-placed items are inserted in the grid
        - gridAutoRows: 规定默认的行尺寸。  Specifies a default row size
        - gridColumn: grid-column-start 和 grid-column-end 属性的简写属性。  A shorthand property for the grid-column-start and the grid-column-end properties
        - gridColumnEnd: 规定如何结束网格项目。  Specifies where to end the grid item
        - gridColumnGap: 规定列间隙的尺寸。  Specifies the size of the gap between columns
        - gridColumnStart: 规定网格项目从何处开始。  Specifies where to start the grid item
        - gridGap: grid-row-gap 和 grid-column-gap 的简写属性。  A shorthand property for the grid-row-gap and grid-column-gap properties
        - gridRow: grid-row-start 和 grid-row-end 属性的简写属性。  A shorthand property for the grid-row-start and the grid-row-end properties
        - gridRowEnd: 规定网格项目在何处结束。  Specifies where to end the grid item
        - gridRowGap: 规定列间隙的尺寸。  Specifies the size of the gap between rows
        - gridRowStart: 规定网格项目从何处开始。  Specifies where to start the grid item
        - gridTemplate: grid-template-rows、grid-template-columns 以及 grid-areas 属性的简写属性。  A shorthand property for the grid-template-rows, grid-template-columns and grid-areas properties
        - gridTemplateAreas: 规定如何使用命名的网格项显示列和行。  Specifies how to display columns and rows, using named grid items
        - gridTemplateColumns: 指定列的尺寸以及网格布局中的列数。  Specifies the size of the columns, and how many columns in a grid layout
        - gridTemplateRows: 指定网格布局中的行的尺寸。  Specifies the size of the rows in a grid layout
        - hangingPunctuation: 规定是否可以在行框外放置标点符号。  Specifies whether a punctuation character may be placed outside the line box
        - height: 设置元素的高度。  Sets the height of an element
        - hyphens: 设置如何分割单词以改善段落的布局。  Sets how to split words to improve the layout of text
        - imageRendering: 当图像被缩放时，向浏览器提供关于保留图像的哪些最重要的方面的信息。  Specifies the type of algorithm to use for image scaling
        - isolation: 定义元素是否必须创建新的堆叠内容。  Defines whether an element must create a new stacking content
        - justifyContent: 规定项目在弹性容器内的对齐方式，当项目未用到所有可用空间时。  Specifies the alignment between the items inside a flexible container when the items do not use all available space
        - justifyItems: 规定网格项在行内方向的对齐方式。在网格容器上设置。  Is set on the grid container. Specifies the alignment of grid items in the inline direction
        - justifySelf: 规定网格项在行内方向的对齐方式。在网格项上设置。  Is set on the grid item. Specifies the alignment of the grid item in the inline direction
        - left: 规定定位元素的左侧位置。  Specifies the left position of a positioned element
        - letterSpacing: 增加或减少文本中的字符间距。  Increases or decreases the space between characters in a text
        - lineBreak: 如何如何/是否换行。  Specifies how/if to break lines
        - lineHeight: 设置行高。  Sets the line height
        - listStyle: 在一条声明中设置所有列表属性。  Sets all the properties for a list in one declaration
        - listStyleImage: 把图像指定为列表项标记。  Specifies an image as the list-item marker
        - listStylePosition: 规定列表项标记的位置。  Specifies the position of the list-item markers (bullet points)
        - listStyleType: 规定列表项标记的类型。  Specifies the type of list-item marker
        - margin: 在一条声明中设置所有外边距属性。  Sets all the margin properties in one declaration
        - marginBottom: 设置元素的下外边距。  Sets the bottom margin of an element
        - marginLeft: 设置元素的左外边距。  Sets the left margin of an element
        - marginRight: 设置元素的右外边距。  Sets the right margin of an element
        - marginTop: 设置元素的上外边距。  Sets the top margin of an element
        - mask: 通过在特定位置遮罩或剪切图像来隐藏元素。  Hides parts of an element by masking or clipping an image at specific places
        - maskType: 规定将遮罩元素用作亮度或 Alpha 遮罩。  Specifies whether an SVG <mask> element is treated as a luminance mask or as an alpha mask
        - maxHeight: 设置元素的最大高度。  Sets the maximum height of an element
        - maxWidth: 设置元素的最大宽度。  Sets the maximum width of an element
        - minHeight: 设置元素的最小高度。  Sets the minimum height of an element
        - minWidth: 设置元素的最小宽度。  Sets the minimum width of an element
        - mixBlendMode: 规定元素内容应如何与其直接父的背景相混合。  Specifies how an element's content should blend with its direct parent background
        - objectFit: 规定替换元素的内容应如何适合其所用高度和宽度建立的框。  Specifies how the contents of a replaced element should be fitted to the box established by its used height and width
        - objectPosition: 指定替换元素在其框内的对齐方式。  Specifies the alignment of the replaced element inside its box
        - opacity: 设置元素的不透明等级。  Sets the opacity level for an element
        - order: 设置弹性项目相对于其余项目的顺序。  Sets the order of the flexible item, relative to the rest
        - orphans: 设置在元素内发生分页时必须保留在页面底部的最小行数。  Sets the minimum number of lines that must be left at the bottom of a page or column
        - outline: outline-width、outline-style 以及 outline-color 属性的简写属性。  A shorthand property for the outline-width, outline-style, and the outline-color properties
        - outlineColor: 设置轮廓的颜色。  Sets the color of an outline
        - outlineOffset: 对轮廓进行偏移，并将其绘制到边框边缘之外。  Offsets an outline, and draws it beyond the border edge
        - outlineStyle: 设置轮廓的样式。  Sets the style of an outline
        - outlineWidth: 设置轮廓的宽度。  Sets the width of an outline
        - overflowWrap: 规定浏览器是否可能为了防止溢出而在单词内折行（当字符串太长而无法适应其包含框时）。  Specifies whether or not the browser can break lines with long words, if they overflow the container
        - overflowX: 规定是否剪裁内容的左右边缘，如果它溢出了元素的内容区域。  Specifies whether or not to clip the left/right edges of the content, if it overflows the element's content area
        - overflowY: 规定是否剪裁内容的上下边缘，如果它溢出了元素的内容区域。  Specifies whether or not to clip the top/bottom edges of the content, if it overflows the element's content area
        - padding: 所有 padding-* 属性的简写属性。  A shorthand property for all the padding-* properties
        - paddingBottom: 设置元素的下内边距。  Sets the bottom padding of an element
        - paddingLeft: 设置元素的左内边距。  Sets the left padding of an element
        - paddingRight: 设置元素的右内边距。  Sets the right padding of an element
        - paddingTop: 设置元素的上内边距。  Sets the top padding of an element
        - pageBreakAfter: 设置元素之后的分页（page-break）行为。  Sets the page-break behavior after an element
        - pageBreakBefore: 设置元素之前的分页（page-break）行为。  Sets the page-break behavior before an element
        - pageBreakInside: 设置元素内的分页（page-break）行为。  Sets the page-break behavior inside an element
        - perspective: 为 3D 定位元素提供透视。  Gives a 3D-positioned element some perspective
        - perspectiveOrigin: 定义用户观看 3D 定位元素的位置。  Defines at which position the user is looking at the 3D-positioned element
        - pointerEvents: 定义元素是否对指针事件做出反应。  Defines whether or not an element reacts to pointer events
        - position: 规定用于元素的定位方法的类型（静态、相对、绝对或固定）。  Specifies the type of positioning method used for an element (static, relative, absolute or fixed)
        - quotes: 设置引号类型。  Sets the type of quotation marks for embedded quotations
        - resize: 定义用户是否以及如何调整元素的尺寸。  Defines if (and how) an element is resizable by the user
        - right: 规定定位元素的左侧位置。  Specifies the right position of a positioned element
        - scrollBehavior: 规定可滚动框中是否平滑地滚动，而不是直接跳跃。  Specifies whether to smoothly animate the scroll position in a scrollable box, instead of a straight jump
        - tabSize: 规定制表符的宽度。  Specifies the width of a tab character
        - tableLayout: 定义用于对单元格、行和列进行布局的算法。  Defines the algorithm used to lay out table cells, rows, and columns
        - textAlign: 规定文本的水平对齐方式。  Specifies the horizontal alignment of text
        - textAlignLast: 描述当 text-align 为 "justify" 时，如何在强制换行之前对齐块或行的最后一行。  Describes how the last line of a block or a line right before a forced line break is aligned when text-align is "justify"
        - textCombineUpright: 将多个字符组合到到单个字符的空间中。  Specifies the combination of multiple characters into the space of a single character
        - textDecoration: 规定文本装饰。  Specifies the decoration added to text
        - textDecorationColor: 规定文本装饰（text-decoration）的颜色。  Specifies the color of the text-decoration
        - textDecorationLine: 规定文本装饰（text-decoration）中的的行类型。  Specifies the type of line in a text-decoration
        - textDecorationStyle: 规定文本装饰（text-decoration）中的行样式。  Specifies the style of the line in a text decoration
        - textIndent: 规定文本块（text-block）中的的首行缩进。  Specifies the indentation of the first line in a text-block
        - textJustify: 规定当 text-align 为 "justify" 时使用的对齐方法。  Specifies the justification method used when text-align is "justify"
        - textOrientation: 定义行中的文本方向。  Defines the orientation of characters in a line
        - textOverflow: 规定当文本溢出包含元素时应该发生的情况。  Specifies what should happen when text overflows the containing element
        - textShadow: 添加文本阴影。  Adds shadow to text 
        - textTransform: 控制文本的大写。  Controls the capitalization of text
        - textUnderlinePosition: 规定使用 text-decoration 属性设置的下划线的位置。  Specifies the position of the underline text decoration
        - top: 规定定位元素的顶端位置。  Specifies the top position of a positioned element
        - transform: 向元素应用 2D 或 3D 转换。  Applies a 2D or 3D transformation to an element
        - transformOrigin: 允许您更改转换元素的位置。  Allows you to change the position on transformed elements
        - transformStyle: 规定如何在 3D 空间中渲染嵌套的元素。  Specifies how nested elements are rendered in 3D space
        - transition: 所有 transition-* 属性的简写属性。  A shorthand property for all the transition-* properties
        - transitionDelay: 规定合适开始过渡效果。  Specifies when the transition effect will start
        - transitionDuration: 规定完成过渡效果所需的秒或毫秒数。  Specifies how many seconds or milliseconds a transition effect takes to complete
        - transitionProperty: 规定过渡效果对应的 CSS 属性的名称。  Specifies the name of the CSS property the transition effect is for
        - transitionTimingFunction: 规定过渡效果的速度曲线。  Specifies the speed curve of the transition effect
        - unicodeBidi: 与 direction 属性一起使用，设置或返回是否应覆写文本来支持同一文档中的多种语言。  Used together with the direction property to set or return whether the text should be overridden to support multiple languages in the same document
        - userSelect: 规定是否能选取元素的文本。  Specifies whether the text of an element can be selected
        - verticalAlign: 设置元素的垂直对齐方式。  Sets the vertical alignment of an element
        - visibility: 规定元素是否可见。  Specifies whether or not an element is visible
        - whiteSpace: 规定如何处理元素内的空白字符。  Specifies how white-space inside an element is handled
        - widows: 设置如果元素内发生分页，必须在页面顶部保留的最小行数。  Sets the minimum number of lines that must be left at the top of a page or column
        - width: 设置元素的宽度。  Sets the width of an element
        - wordBreak: 规定单词到达行末后如何换行。  Specifies how words should break when reaching the end of a line
        - wordSpacing: 增加或减少文本中的单词间距。  Increases or decreases the space between words in a text
        - wordWrap: 允许长的、不能折行的单词换到下一行。  Allows long, unbreakable words to be broken and wrap to the next line
        - writingMode: 规定文本行是水平还是垂直布局。  Specifies whether lines of text are laid out horizontally or vertically
        - zIndex: 设置定位元素的堆叠顺序。  Sets the stack order of a positioned element
"""

    frame = inspect.currentframe()
    try:
        if frame is not None:
            argvalues = inspect.getargvalues(frame)
            args_dict = dict(argvalues.locals)
            kwargs = args_dict.pop('kwargs', {})
            # 去除None值属性
            args = {key: value for key, value in args_dict.items() if value is not None and key not in ['rawCSS', 'frame', 'argvalues', 'args_dict']}
        else:
            # 如果无法获取帧信息，则使用空字典
            args = {}
            kwargs = {}
    finally:
        if frame is not None:
            del frame

    # 处理针对rawCSS的自动解析
    args_from_css = {}
    if rawCSS:
        css_rules = parseString(rawCSS)
        for rule in css_rules:
            if rule.type == rule.STYLE_RULE:
                args_from_css = {
                    css_prop.name: css_prop.value
                    for css_prop in rule.style
                }
    # 将args_from_css中的键名格式转换为小驼峰格式
    args_from_css = {
        ''.join(
            [
                s if i == 0 else s.capitalize()
                for i, s in enumerate(key.split('-'))
            ]
        ): value
        for key, value in args_from_css.items()
    }

    return {**args_from_css, **args, **kwargs}
