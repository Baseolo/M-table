<?php
try{
require('proc_avvia_sessione.php');
require('proc_funzioni.php');
require('proc_database.php');
require('proc_addlog.php');
$amks_operazione = 'Visualizzazione';
if (isset($_GET['codice'])) {
   $_SESSION['codice'] = $_GET['codice'];
}
require('proc_testata.php');
echo '<div class="funzioni">Appalti - '.$amks_operazione.'</div>';
vis_riga_anagrafe($_SESSION['codice']);
genera_form('esegui.php?d=d',"100%");
echo '<table>';
echo '<thead>  <tr>  <th>Descrizione</th> <th>Data inizio</th>  <th>Data fine</th><th>Funzioni</th> </tr> </thead>';
echo ' <tbody> ';
if ($_SESSION['app'] == 'S') echo ' <tr> <td>Aggiungi nuovo appalto</td> <td></td> <td></td> <td> <a href="appalti.php?fnz=add&codice='.$_SESSION['codice'].'&amk='.$_SESSION['amk'].'"><img class="azioni" src="immagini/add.png"></a></td></tr>';
foreach ($pdo->query("SELECT * FROM appalti WHERE anagrafe={$_SESSION['codice']}") as $r) {
    echo ' <tr> <td>'.$r['descrizione'].'</td> <td>'.implode('/',array_reverse(explode('-',$r['data_inizio']))).'</td> <td>'.implode('/',array_reverse(explode('-',$r['data_fine']))).'</td> <td width="178px">';
    genera_azione('appalti_riep.php?codice='.$r['codice'].'&amk='.$_SESSION['amk'],"immagini/riep.png");   
    if ($_SESSION['app'] == 'S') genera_azione('servizi_vis.php?codice='.$r['codice'].'&amk='.$_SESSION['amk'],"immagini/servizi.png");
    echo '</td></tr>';
   }
echo ' </tbody> </table>';
} catch (PDOException $e) {gestione_errori_try("Errore imprevisto riga " . $e->getLine ( ) . $e->getFile ( ) ." ".$e->getMessage());}
?>
