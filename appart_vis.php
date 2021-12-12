<?php
try{
require('proc_avvia_sessione.php');
require('proc_funzioni.php');
require('proc_database.php');
require('proc_addlog.php');
if (isset($_GET['codice'])) { $_SESSION['codice'] = $_GET['codice'];  }
$amka_codice = $_SESSION['codice'];    
require('proc_testata.php');
echo '<div class="funzioni">Articoli utilizzati per l\'appalto</div>';
$r_app = $pdo->query("SELECT * FROM appalti WHERE codice={$_SESSION['codice']}")->fetch();
vis_riga_anagrafe($r_app['anagrafe']);
vis_riga_appalto($r_app['codice']);
genera_form('esegui.php?d=d','100%'); 
echo '<table>';
echo '<thead>  <tr> <th width="35%">Descrizione</th> <th width="18%">Categoria</th> <th width="12%">Unit&agrave; di misura</th> <th width="10%">Foto</th><th width="10%">Immagini</th><th width="20%">Allegati</th></tr> </thead>';
echo ' <tbody> ';
foreach ($pdo->query("SELECT * FROM articoli Order by descrizione ASC") as $r_art) {
    if ( $pdo->query("SELECT count(*) FROM appart WHERE appalto='{$_SESSION['codice']}' AND articolo='{$r_art['codice']}'")->fetchColumn() > 0) {
        echo '<td  style="height:100px;" >'.$r_art['descrizione'].'</td>  <td>'.dammi_categoria($r_art['categoria']).'</td> <td>'.$r_art['unita_misura'].'</td></td> </td>';
        echo '<td style="text-align:center;">';
        $amka_codice = $r_art['codice'];    
        $amka_cartella = dammi_cartella_articoli($amka_codice);       
        foreach (glob($amka_cartella . 'foto' . $amka_codice . '_*.*') as $f) genera_azione('visualizza_foto.php?file=' . $f .'&fnz=vis&amk=' . $_SESSION['amk'], $f);
        echo '</td><td style="text-align:center;">';        
        foreach (glob($amka_cartella . 'immagine' . $amka_codice . '_*.*') as $f) genera_azione_img('visualizza_immagine.php?file=' . $f .'&fnz=vis&amk=' . $_SESSION['amk'], $f);
        echo '</td><td>';    
        foreach (glob($amka_cartella . 'allegato' . $amka_codice . '_*.*') as $f) {
            $r_all = $pdo->query("SELECT * FROM allegati WHERE nomefile='$f'")->fetch();
            genera_azione_pdf('visualizza_allegato.php?file=' . $f . '&fnz=vis&amk=' . $_SESSION['amk'],$r_all['descrizione']);
            echo '<br>';
        }
    echo '</td></tr>';
   }
}
echo ' </tbody> </table>';
} catch (PDOException $e) {gestione_errori_try("Errore imprevisto riga " . $e->getLine ( ) . $e->getFile ( ) ." ".$e->getMessage());}
?>
