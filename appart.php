<?php
try{
require('proc_avvia_sessione.php');
require('proc_funzioni.php');
require('proc_database.php');
require('proc_addlog.php');
$amkf_descrizione = '';
$amkf_categoria = 0;
if (isset($_POST['ricerca'])) {
    $amkf_descrizione = sanifica_stringa($_POST['campo01']);
    $amkf_categoria = $_POST['campo02'];
}
if (isset($_GET['codice'])) {
   $_SESSION['codice'] = $_GET['codice'];
}
require('proc_testata.php');
echo '<div class="funzioni">Gestione collegamenti appalto / articoli </div>';
$r_app = $pdo->query("SELECT * FROM appalti WHERE codice={$_SESSION['codice']}")->fetch();
vis_riga_anagrafe($r_app['anagrafe']);
vis_riga_appalto($r_app['codice']);
echo '<br>';
echo '<div class="form-ricerca"> <form method="post" action="appart.php?amk='.$_SESSION['amk'].'" onkeypress="return (event.keyCode!=13)"  >';
echo '<div class="funzioni">Elenco articoli collegati</div>';
echo '<table>';
echo '<thead>  <tr>  <th width="44%">Descrizione articolo</th> <th width="34%">Categoria</th>  <th  width="20%">Unit&agrave; di misura</th> <th>Azioni</th></tr> </thead>';
echo ' <tbody> ';
foreach ($pdo->query("SELECT * FROM articoli ORDER BY descrizione") as $r_art) {
    $r_apa = $pdo->query("SELECT * FROM appart WHERE appalto={$_SESSION['codice']} AND articolo={$r_art['codice']}")->fetch();    
    if (is_array($r_apa)) {
        echo '<td>'.$r_art['descrizione'].'</td>  <td>'.dammi_categoria($r_art['categoria']).'</td>  <td>'.$r_art['unita_misura'].'</td>  <td>';
        genera_azione('appart_del.php?codice='.$r_apa['codice'].'&amk='.$_SESSION['amk'],"immagini/del.png");
        echo '</td>  </tr>';
    }
}
echo ' </tbody> </table>';
echo '<br>';
echo '<br>';
echo '<br>';
echo '<div class="funzioni">Elenco articoli non collegati</div>';
echo 'descrizione <input type="text" placeholder="descrizione" name="campo01" value="'.$amkf_descrizione.'" autocomplete="off">';
echo ' categoria <select name="campo02" >';
echo '<option value="0">Tutte le categorie</option>';
foreach ($pdo->query("SELECT * FROM catart") as $r_car) {
   echo '<option value="'.$r_car['codice'].'" ';
   if ($amkf_categoria == $r_car['codice']) { echo 'selected';}
   echo '>'.$r_car['descrizione'].'</option>'; 
}
echo '   </select> ';
echo '<input class="bottone_aggiorna" type="submit" name="ricerca" value="Aggiorna" > ';
echo '<table>';
echo '<thead>  <tr>  <th width="44%">Descrizione articolo</th> <th width="34%">Categoria</th>  <th width="20%">Unit&agrave; di misura</th> <th>Azioni</th></tr> </thead>';
echo ' <tbody> ';
$condizione = '';
if (!empty($amkf_descrizione)) {if(empty($condizione)) {$condizione .= " WHERE descrizione LIKE '%$amkf_descrizione%'"; } else {$condizione .= " AND descrizione LIKE '%$amkf_descrizione%'"; } }
if ($amkf_categoria <> 0) {if(empty($condizione)) {$condizione .= " WHERE categoria =$amkf_categoria"; } else {$condizione .= " AND categoria LIKE '%$amkf_categoria%'"; } }
foreach ($pdo->query("SELECT * from articoli $condizione ORDER BY descrizione") as $r_art) {
    if ( $pdo->query("SELECT count(*) FROM appart WHERE appalto='{$_SESSION['codice']}' AND articolo='{$r_art['codice']}'")->fetchColumn() == 0) {
        echo '<td>'.$r_art['descrizione'].'</td>  <td>'.dammi_categoria($r_art['categoria']).'</td> <td>'.$r_art['unita_misura'].'</td><td>';
        genera_azione('appart_add.php?codice='.$r_art['codice'].'&amk='.$_SESSION['amk'],"immagini/add.png");
        echo '</td>  </tr>';
    }
}
echo ' </tbody> </table>';
} catch (PDOException $e) {gestione_errori_try("Errore imprevisto riga " . $e->getLine ( ) . $e->getFile ( ) ." ".$e->getMessage());}
?>
