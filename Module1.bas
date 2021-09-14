Attribute VB_Name = "Module1"
Sub Макрос1()
Attribute Макрос1.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Макрос1 Макрос
'

'
    Range("A1:E1").Select
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlBottom
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 90
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Range("F1").Select
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 90
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Range("H1:N1").Select
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 90
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Rows("1:1").Select
    With Selection
        .HorizontalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Columns("A:A").Select
    Selection.TextToColumns Destination:=Range("A1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=False, FieldInfo _
        :=Array(1, 1), TrailingMinusNumbers:=True
    Columns("N:N").Select
    Selection.TextToColumns Destination:=Range("N1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=False, FieldInfo _
        :=Array(1, 1), TrailingMinusNumbers:=True
    Columns("I:I").Select
    Selection.TextToColumns Destination:=Range("I1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=False, FieldInfo _
        :=Array(1, 1), TrailingMinusNumbers:=True
    Columns("J:J").Select
    Selection.TextToColumns Destination:=Range("J1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=False, FieldInfo _
        :=Array(1, 1), TrailingMinusNumbers:=True
    Range("A1:M1497").Select
    ActiveWindow.SmallScroll Down:=-45
    ActiveWindow.ScrollRow = 1407
    ActiveWindow.ScrollRow = 1403
    ActiveWindow.ScrollRow = 1401
    ActiveWindow.ScrollRow = 1395
    ActiveWindow.ScrollRow = 1391
    ActiveWindow.ScrollRow = 1380
    ActiveWindow.ScrollRow = 1374
    ActiveWindow.ScrollRow = 1358
    ActiveWindow.ScrollRow = 1249
    ActiveWindow.ScrollRow = 1206
    ActiveWindow.ScrollRow = 1189
    ActiveWindow.ScrollRow = 1166
    ActiveWindow.ScrollRow = 913
    ActiveWindow.ScrollRow = 861
    ActiveWindow.ScrollRow = 630
    ActiveWindow.ScrollRow = 613
    ActiveWindow.ScrollRow = 596
    ActiveWindow.ScrollRow = 571
    ActiveWindow.ScrollRow = 548
    ActiveWindow.ScrollRow = 528
    ActiveWindow.ScrollRow = 268
    ActiveWindow.ScrollRow = 234
    ActiveWindow.ScrollRow = 54
    ActiveWindow.ScrollRow = 29
    ActiveWindow.ScrollRow = 1
    Rows("1:1").Select
    With ActiveWindow
        .SplitColumn = 0
        .SplitRow = 1
    End With
    ActiveWindow.FreezePanes = True
    Application.CutCopyMode = False
    Application.PrintCommunication = False
    With ActiveSheet.PageSetup
        .PrintTitleRows = "$1:$1"
        .PrintTitleColumns = ""
    End With
    Application.PrintCommunication = True
    ActiveSheet.PageSetup.PrintArea = ""
    Application.PrintCommunication = False
    With ActiveSheet.PageSetup
        .LeftHeader = ""
        .CenterHeader = "&P"
        .RightHeader = ""
        .LeftFooter = ""
        .CenterFooter = "&F"
        .RightFooter = ""
        .LeftMargin = Application.InchesToPoints(0.31496062992126)
        .RightMargin = Application.InchesToPoints(0.31496062992126)
        .TopMargin = Application.InchesToPoints(0.590551181102362)
        .BottomMargin = Application.InchesToPoints(0.354330708661417)
        .HeaderMargin = Application.InchesToPoints(0.118110236220472)
        .FooterMargin = Application.InchesToPoints(0.118110236220472)
        .PrintHeadings = False
        .PrintGridlines = False
        .PrintComments = xlPrintNoComments
        .CenterHorizontally = True
        .CenterVertically = False
        .Orientation = xlPortrait
        .Draft = False
        .PaperSize = xlPaperA4
        .FirstPageNumber = 1
        .Order = xlOverThenDown
        .BlackAndWhite = False
        .Zoom = 100
        .PrintErrors = xlPrintErrorsDisplayed
        .OddAndEvenPagesHeaderFooter = False
        .DifferentFirstPageHeaderFooter = False
        .ScaleWithDocHeaderFooter = True
        .AlignMarginsHeaderFooter = False
        .EvenPage.LeftHeader.Text = ""
        .EvenPage.CenterHeader.Text = ""
        .EvenPage.RightHeader.Text = ""
        .EvenPage.LeftFooter.Text = ""
        .EvenPage.CenterFooter.Text = ""
        .EvenPage.RightFooter.Text = ""
        .FirstPage.LeftHeader.Text = ""
        .FirstPage.CenterHeader.Text = ""
        .FirstPage.RightHeader.Text = ""
        .FirstPage.LeftFooter.Text = ""
        .FirstPage.CenterFooter.Text = ""
        .FirstPage.RightFooter.Text = ""
    End With
    Application.PrintCommunication = True
    Range("A1:M354").Select
    ActiveWindow.ScrollRow = 334
    ActiveWindow.ScrollRow = 333
    ActiveWindow.ScrollRow = 332
    ActiveWindow.ScrollRow = 331
    ActiveWindow.ScrollRow = 329
    ActiveWindow.ScrollRow = 328
    ActiveWindow.ScrollRow = 326
    ActiveWindow.ScrollRow = 325
    ActiveWindow.ScrollRow = 322
    ActiveWindow.ScrollRow = 321
    ActiveWindow.ScrollRow = 317
    ActiveWindow.ScrollRow = 315
    ActiveWindow.ScrollRow = 311
    ActiveWindow.ScrollRow = 309
    ActiveWindow.ScrollRow = 233
    ActiveWindow.ScrollRow = 225
    ActiveWindow.ScrollRow = 211
    ActiveWindow.ScrollRow = 203
    ActiveWindow.ScrollRow = 154
    ActiveWindow.ScrollRow = 149
    ActiveWindow.ScrollRow = 138
    ActiveWindow.ScrollRow = 134
    ActiveWindow.ScrollRow = 126
    ActiveWindow.ScrollRow = 72
    ActiveWindow.ScrollRow = 62
    ActiveWindow.ScrollRow = 58
    ActiveWindow.ScrollRow = 54
    ActiveWindow.ScrollRow = 51
    ActiveWindow.ScrollRow = 32
    ActiveWindow.ScrollRow = 31
    ActiveWindow.ScrollRow = 28
    ActiveWindow.ScrollRow = 27
    ActiveWindow.ScrollRow = 26
    ActiveWindow.ScrollRow = 25
    ActiveWindow.ScrollRow = 24
    ActiveWindow.ScrollRow = 23
    ActiveWindow.ScrollRow = 21
    ActiveWindow.ScrollRow = 20
    ActiveWindow.ScrollRow = 19
    ActiveWindow.ScrollRow = 18
    ActiveWindow.ScrollRow = 16
    ActiveWindow.ScrollRow = 15
    ActiveWindow.ScrollRow = 14
    ActiveWindow.ScrollRow = 13
    ActiveWindow.ScrollRow = 12
    ActiveWindow.ScrollRow = 11
    ActiveWindow.ScrollRow = 10
    ActiveWindow.ScrollRow = 9
    ActiveWindow.ScrollRow = 7
    ActiveWindow.ScrollRow = 2
    Range("A1:N86").Select
    ActiveWindow.SmallScroll Down:=-114
    Application.CutCopyMode = False
    ActiveSheet.ListObjects.Add(xlSrcRange, Range("$A$1:$N$86"), , xlYes).Name = _
        "Таблица1"
    Range("A1:N86").Select
    ActiveSheet.ListObjects("Таблица1").TableStyle = "TableStyleMedium4"
    Columns("A:F").Select
    Selection.ColumnWidth = 7.14
    Selection.ColumnWidth = 5
    Columns("A:N").Select
    With Selection
        .HorizontalAlignment = xlGeneral
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With Selection
        .HorizontalAlignment = xlCenter
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlBottom
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Range("A1:N86").Select
    Range("E1").Activate
    ActiveWindow.SmallScroll Down:=-129
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideVertical)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideHorizontal)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    ActiveWindow.View = xlPageBreakPreview
    ActiveSheet.VPageBreaks(1).DragOff Direction:=xlToRight, RegionIndex:=1
    Range("H1").Select
    ActiveWindow.SmallScroll Down:=-99
    ActiveWindow.FreezePanes = False
    ActiveWindow.View = xlNormalView
    ActiveWindow.View = xlPageLayoutView
    Application.PrintCommunication = False
    With ActiveSheet.PageSetup
        .LeftHeader = ""
        .CenterHeader = "&P"
        .RightHeader = ""
        .LeftFooter = ""
        .CenterFooter = "&F"
        .RightFooter = ""
        .LeftMargin = Application.InchesToPoints(0.31496062992126)
        .RightMargin = Application.InchesToPoints(0.31496062992126)
        .TopMargin = Application.InchesToPoints(0.590551181102362)
        .BottomMargin = Application.InchesToPoints(0.354330708661417)
        .HeaderMargin = Application.InchesToPoints(0.118110236220472)
        .FooterMargin = Application.InchesToPoints(0.118110236220472)
        .Zoom = 65
        .PrintErrors = xlPrintErrorsDisplayed
        .OddAndEvenPagesHeaderFooter = False
        .DifferentFirstPageHeaderFooter = False
        .ScaleWithDocHeaderFooter = True
        .AlignMarginsHeaderFooter = False
        .EvenPage.LeftHeader.Text = ""
        .EvenPage.CenterHeader.Text = ""
        .EvenPage.RightHeader.Text = ""
        .EvenPage.LeftFooter.Text = ""
        .EvenPage.CenterFooter.Text = ""
        .EvenPage.RightFooter.Text = ""
        .FirstPage.LeftHeader.Text = ""
        .FirstPage.CenterHeader.Text = ""
        .FirstPage.RightHeader.Text = ""
        .FirstPage.LeftFooter.Text = ""
        .FirstPage.CenterFooter.Text = ""
        .FirstPage.RightFooter.Text = ""
    End With
    Application.PrintCommunication = True
    Application.PrintCommunication = False
    With ActiveSheet.PageSetup
        .LeftHeader = "&P/&N"
        .CenterHeader = "&F"
        .RightHeader = "&D"
        .LeftFooter = ""
        .CenterFooter = "&F"
        .RightFooter = ""
        .LeftMargin = Application.InchesToPoints(0.31496062992126)
        .RightMargin = Application.InchesToPoints(0.31496062992126)
        .TopMargin = Application.InchesToPoints(0.590551181102362)
        .BottomMargin = Application.InchesToPoints(0.354330708661417)
        .HeaderMargin = Application.InchesToPoints(0.118110236220472)
        .FooterMargin = Application.InchesToPoints(0.118110236220472)
        .Zoom = 65
        .PrintErrors = xlPrintErrorsDisplayed
        .OddAndEvenPagesHeaderFooter = False
        .DifferentFirstPageHeaderFooter = False
        .ScaleWithDocHeaderFooter = True
        .AlignMarginsHeaderFooter = False
        .EvenPage.LeftHeader.Text = ""
        .EvenPage.CenterHeader.Text = ""
        .EvenPage.RightHeader.Text = ""
        .EvenPage.LeftFooter.Text = ""
        .EvenPage.CenterFooter.Text = ""
        .EvenPage.RightFooter.Text = ""
        .FirstPage.LeftHeader.Text = ""
        .FirstPage.CenterHeader.Text = ""
        .FirstPage.RightHeader.Text = ""
        .FirstPage.LeftFooter.Text = ""
        .FirstPage.CenterFooter.Text = ""
        .FirstPage.RightFooter.Text = ""
    End With
    Application.PrintCommunication = True
    Range("G2").Select
    ActiveWindow.SmallScroll Down:=-81
End Sub
