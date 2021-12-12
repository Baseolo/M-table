<?php
try{
require('proc_avvia_sessione.php');
require('proc_funzioni.php');
require('proc_database.php');
require('proc_addlog.php');
$r_art = $pdo->query("SELECT * FROM articoli WHERE codice={$_GET['codice']}")->fetch();
$pdo->exec("INSERT INTO appart (appalto, articolo) VALUES ({$_SESSION['codice']},{$_GET['codice']})");
aggiorna_operazioni('appart',$pdo->lastInsertId(),'Inserimento',$r_art['descrizione']);     
header('Location: '.$_SESSION['ritorno'].'&amk='.$_SESSION['amk']);
exit;
} catch (PDOException $e) {gestione_errori_try("Errore imprevisto riga " . $e->getLine ( ) . $e->getFile ( ) ." ".$e->getMessage());}
?>
