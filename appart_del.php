<?php
try{
require('proc_avvia_sessione.php');
require('proc_funzioni.php');
require('proc_database.php');
require('proc_addlog.php');
$pdo->exec("DELETE FROM appart  WHERE codice={$_GET['codice']}");
aggiorna_operazioni('appart',$_GET['codice'],'Cancellazione','');     
//header('Location: appart.php?amk='  . $_SESSION['amk']);  
header('Location: '.$_SESSION['ritorno'].'&amk='.$_SESSION['amk']);
exit;
} catch (PDOException $e) {gestione_errori_try("Errore imprevisto riga " . $e->getLine ( ) . $e->getFile ( ) ." ".$e->getMessage());}
?>
