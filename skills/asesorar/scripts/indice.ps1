param([string]$ruta)
# Rellena con Word el indice automatico y los indices de tablas y figuras, igual que
# "Actualizar tabla > Actualizar toda la tabla": abre el documento en una instancia aparte,
# actualiza los campos y guarda. No retoca el formato. Imprime las entradas para comprobarlas.
# La ruta tiene que ser completa. El documento no puede estar abierto en otro Word.
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
    $d = $w.Documents.Open($ruta, $false, $false)
    $d.Repaginate()
    $d.Fields.Update() | Out-Null
    foreach ($t in $d.TablesOfContents) { $t.Update() }
    foreach ($t in $d.TablesOfFigures) { $t.Update() }
    "indices: $($d.TablesOfContents.Count) - de tablas o figuras: $($d.TablesOfFigures.Count) - paginas: $($d.ComputeStatistics(2))"
    foreach ($t in $d.TablesOfContents) { $t.Range.Text -split "`r" }
    foreach ($t in $d.TablesOfFigures) { "--- tabla de ilustraciones"; $t.Range.Text -split "`r" }
    $d.Save()
    $d.Close($false)
} finally {
    if ($w.Documents.Count -eq 0) { $w.Quit() }
    [void][Runtime.InteropServices.Marshal]::ReleaseComObject($w)
}
