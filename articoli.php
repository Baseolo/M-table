<?php
try {
    require('proc_avvia_sessione.php');
    require('proc_funzioni.php');
    require('proc_database.php');
    require('proc_addlog.php');
    $amks_azione = 'articoli.php?fnz=' . $_GET['fnz'];
// -------------------- impostazione descrizione operazione e descrizione bottone per visualizzazione form ----------------------------------------    
    if ($_GET['fnz'] == 'add') { $amks_operazione = 'Inserimento'; $amks_bottone = 'Inserisci'; }
    if ($_GET['fnz'] == 'var') { $amks_operazione = 'Variazione';  $amks_bottone = 'Modifica';  }
    if ($_GET['fnz'] == 'del') { $amks_operazione = 'Cancellazione'; $amks_bottone = 'Elimina'; }
    if ($_GET['fnz'] == 'vis') { $amks_operazione = 'Visualizzazione'; $amks_bottone = '';      }
// ------------------- pulizia dei campi ---------------------------------------------------------------------
    $amkf_descrizione = '';
    $amkf_categoria = 0;    
    $amkf_unita_misura = '';
    $amkf_qta_confezione = 1;    
    $amkf_prezzo = 0;        
    $amkf_giacenza_minima = 0;        
    $amkf_note = '';      
    $amkf_barcode = '';          
// ------------ se presente codice (prima chiamata del programma) imposta campi da record
    if (isset($_GET['codice'])) {
        $_SESSION['codice'] = $_GET['codice'];
        $amka_dipendente = $_SESSION['codice_utente'];        
        unset($_SESSION['bac_descrizione']);
        pulisci_appoggio();
// ----------- impostazione dei campi tramite del form da record se variazione cancellazione o visualizzazione -----------------------------    
        if ($_GET['fnz'] == 'var' or $_GET['fnz'] == 'vis' or $_GET['fnz'] == 'del' ) {
            $r_art = $pdo->query("SELECT * FROM articoli WHERE codice={$_SESSION['codice']}")->fetch();
            $amkf_descrizione = $r_art['descrizione'];
            $amkf_categoria = $r_art['categoria'];            
            $amkf_unita_misura = $r_art['unita_misura'];
            $amkf_prezzo = $r_art['prezzo'];            
            $amkf_giacenza_minima = $r_art['giacenza_minima'];                        
            $amkf_qta_confezione = $r_art['qta_confezione'];               
            $amkf_note = $r_art['note'];                
            $amkf_barcode = $r_art['barcode'];                
            $_SESSION['bac_descrizione'] = $amkf_descrizione;
            $_SESSION['bac_categoria'] = $amkf_categoria;            
            $_SESSION['bac_unita_misura'] = $amkf_unita_misura;
            $_SESSION['bac_qta_confezione'] = $amkf_qta_confezione;            
            $_SESSION['bac_prezzo'] = $amkf_prezzo;                        
            $_SESSION['bac_giacenza_minima'] = $amkf_giacenza_minima;   
            $_SESSION['bac_note'] = $amkf_note;                                        
            $_SESSION['bac_barcode'] = $amkf_barcode;   
            $amka_codice = $_GET['codice'];
            $amka_cartella = dammi_cartella_articoli($amka_codice);        
            da_cartella_ad_appoggio($amka_cartella, $amka_codice);
        }
    }

// impostazione dei campi da appoggio su sessione se presenti (per quando si ritorna da altri programmi) ----------------------------------------------------    
    if (!isset($_POST['campo01']) and isset($_SESSION['bac_descrizione'])){
        $amkf_descrizione = $_SESSION['bac_descrizione'];
        $amkf_categoria = $_SESSION['bac_categoria'];        
        $amkf_qta_confezione = $_SESSION['bac_qta_confezione'];        
        $amkf_prezzo = $_SESSION['bac_prezzo'];        
        $amkf_giacenza_minima = $_SESSION['bac_giacenza_minima'];                
        $amkf_barcode = $_SESSION['bac_barcode'];
        $amkf_note = $_SESSION['bac_note'];        
        $amkf_unita_misura = $_SESSION['bac_unita_misura'];                                
    }
// ----------- impostazione dei campi con dati ricevuti dal form ------------------------------------------------------------------
    if (isset($_POST['campo01']) and !isset($_GET['codice']) ) {   
        $amkf_descrizione = sanifica_stringa($_POST['campo01']);
        $amkf_categoria = sanifica_stringa($_POST['campo07']);        
        $amkf_unita_misura = sanifica_stringa($_POST['campo02']);                
        if ($_SESSION['app'] == 'S') $amkf_note = sanifica_stringa($_POST['campo99']);        
        $amkf_prezzo = str_replace(',','.',sanifica_stringa($_POST['campo04']));
        $amkf_giacenza_minima = str_replace(',','.',sanifica_stringa($_POST['campo05']));
        $amkf_qta_confezione = str_replace(',','.',sanifica_stringa($_POST['campo03']));
        $amkf_barcode = sanifica_stringa($_POST['campo06']);        
        $_SESSION['bac_descrizione'] = $amkf_descrizione;
        $_SESSION['bac_categoria'] = $amkf_categoria;        
        $_SESSION['bac_unita_misura'] = $amkf_unita_misura;
        $_SESSION['bac_qta_confezione'] = $amkf_qta_confezione;            
        $_SESSION['bac_prezzo'] = $amkf_prezzo;                        
        $_SESSION['bac_giacenza_minima'] = $amkf_giacenza_minima;                                
        $_SESSION['bac_note'] = $amkf_note;                                        
        $_SESSION['bac_barcode'] = $amkf_barcode;        
    }
// ---------- gestione richieste allega foto immagine  o pdf --------------------------------------------------------   
    if (isset($_GET['azione'])) { 
        if ($_GET['azione'] == 'allegato') { header('Location: visualizza_allegato.php?file=' . $_GET['nomefile'] . '&fnz='.$_GET['fnz'].'&amk='  . $_SESSION['amk']);   exit;  }
        if ($_GET['azione'] == 'foto') { header('Location: visualizza_foto.php?file=' . $_GET['nomefile'] . '&fnz='.$_GET['fnz'].'&amk='  . $_SESSION['amk']);   exit;   }
        if ($_GET['azione'] == 'immagine') { header('Location: visualizza_immagine.php?file=' . $_GET['nomefile'] . '&fnz='.$_GET['fnz'].'&amk='  . $_SESSION['amk']);   exit;   }
    } 
    if (isset($_POST['foto'])) { header('Location: scatta_foto.php?amk=' . $_SESSION['amk']);   exit; }
    if (isset($_POST['immagine'])) { header('Location: upload_immagine.php?amk=' . $_SESSION['amk']);   exit; }    
    if (isset($_POST['allegato'])) { header('Location: upload_allegato.php?amk=' . $_SESSION['amk']); exit;  }
    $_SESSION['barcode'] = $amkf_barcode;    
// ----------- in presenza di dati e quindi aggiornamento archivi se non ci sono errori ----------------------    
    if (isset($_POST['dati'])) {
         if ($_GET['fnz'] == 'add' or$_GET['fnz'] == 'var')  {
            if (empty($amkf_descrizione)) imposta_errore('Descrizione obbligatoria');
            if (empty($amkf_unita_misura)) imposta_errore('Unit&agrave; di misura obbligatoria');     
            if (!is_numeric($amkf_qta_confezione)) {imposta_errore('Quantit&agrave; per confezione errata');}        
            if (!is_numeric($amkf_prezzo)) {imposta_errore('Prezzo errato');}                
            if (!is_numeric($amkf_giacenza_minima)) {imposta_errore('Giacenza minima errata');}                        
            if (strlen($amkf_descrizione) > 250) imposta_errore('Lunghezza descrizione oltre i 250 caratteri');
            if (strlen($amkf_unita_misura) > 250) imposta_errore('Lunghezza Unit&agrave; di misura oltre i 250 caratteri');        
            if (strlen($amkf_barcode) > 50) imposta_errore('Lunghezza barcode oltre i 50 caratteri');                
            if (strlen($amkf_note) > 500) imposta_errore('Lunghezza note oltre i 500 caratteri');        
            if (!empty($amkf_barcode)) {
                $r_art = $pdo->query("SELECT * FROM articoli WHERE barcode='$amkf_barcode'")->fetch();
                if (is_array($r_art) ) {
                    if ($r_art['codice'] <> $_SESSION['codice'])
                        imposta_errore('Barcode gi&agrave; utilizzato');
                }
            }
            if (empty($amks_errore)) {
                if ($amkf_prezzo < 0) imposta_errore('Il prezzo non pu&ograve; essere minore di zero');        
                if ($amkf_qta_confezione < 1) imposta_errore('La Quantit&agrave; per confezione non pu&ograve; essere minore di 1');                    
                if ($amkf_giacenza_minima < 0) imposta_errore('La giacenza minima non pu&ograve; essere negativa');                                
            }
         }
         if ($_GET['fnz'] == 'del') {
            $amka_codice = $_SESSION['codice'];             
            if ($pdo->query("SELECT count(*) FROM appart WHERE articolo='$amka_codice'")->fetchColumn() > 0) imposta_errore('Articolo collegato ad appalto ');         
            if ($pdo->query("SELECT count(*) FROM movimenti WHERE articolo='$amka_codice'")->fetchColumn() > 0) imposta_errore('Articolo movimentato');                     
            if ($pdo->query("SELECT count(*) FROM prenotazioni WHERE articolo='$amka_codice'")->fetchColumn() > 0) imposta_errore('Articolo in fase di prenotazione');                                 
            if ($pdo->query("SELECT count(*) FROM colatr WHERE articolo='$amka_codice'")->fetchColumn() > 0) imposta_errore('Articolo utilizzato negli attrezzi');                                             
            if ($pdo->query("SELECT count(*) FROM movattr WHERE articolo='$amka_codice'")->fetchColumn() > 0) imposta_errore('Articolo movimentato come attrezzo');                                                         
         }
        if (empty($amks_errore)) {
            $amka_timestamp = time();
            if ($_GET['fnz'] == 'add') {
                $pdo->exec("INSERT INTO articoli (descrizione,categoria,unita_misura,prezzo,qta_confezione,barcode,giacenza_minima,note) VALUES ('$amkf_descrizione',$amkf_categoria,'$amkf_unita_misura','$amkf_prezzo','$amkf_qta_confezione','$amkf_barcode','$amkf_giacenza_minima','$amkf_note')");
                $amka_codice_scritto = $pdo->lastInsertId();
                aggiorna_operazioni('articoli',$amka_codice_scritto,'Inserimento',$amkf_descrizione);
                if (empty($amkf_barcode)) {
                    $amkf_barcode = 'ART'.str_pad($amka_codice_scritto,10,'0',STR_PAD_LEFT);
                    $pdo->query("UPDATE articoli SET  barcode='$amkf_barcode' WHERE codice='$amka_codice_scritto'");                
                }
                $amka_cartella = dammi_cartella_articoli($amka_codice_scritto);
                da_appoggio_a_cartella($amka_cartella, $amka_codice_scritto);
                $amks_eseguito = 'Inserimento ' . $amkf_descrizione .' effettuato ';
                $amkf_descrizione = '';
                $amkf_categoria = 0;    
                $amkf_unita_misura = '';
                $amkf_qta_confezione = 1;    
                $amkf_prezzo = 0;        
                $amkf_giacenza_minima = 0;        
                $amkf_note = '';      
                $amkf_barcode = '';         
                unset($_SESSION['bac_descrizione']);                
            }
            if ($_GET['fnz'] == 'var') {
                $amka_codice = $_SESSION['codice'];  
                $amka_cartella = dammi_cartella_articoli($amka_codice);                
                $pdo->query("UPDATE articoli SET descrizione='$amkf_descrizione',categoria='$amkf_categoria',unita_misura='$amkf_unita_misura',prezzo='$amkf_prezzo',qta_confezione='$amkf_qta_confezione',giacenza_minima='$amkf_giacenza_minima', barcode='$amkf_barcode', note='$amkf_note' WHERE codice='$amka_codice'");
                aggiorna_operazioni('articoli',$amka_codice,'Variazione',$amkf_descrizione);                
                if (empty($amkf_barcode)) {
                    $amkf_barcode = 'ART'.str_pad($amka_codice,10,'0',STR_PAD_LEFT);
                    $pdo->query("UPDATE articoli SET  barcode='$amkf_barcode' WHERE codice='$amka_codice'");                
                }
                cancella_cartella($amka_cartella, $amka_codice);
                da_appoggio_a_cartella($amka_cartella, $amka_codice);
                $amks_eseguito = 'Variazione ' . $amkf_descrizione . ' effettuata ';
                require('proc_ritorno.php');
                exit;
            }
            if ($_GET['fnz'] == 'del') {
                $amka_codice = $_SESSION['codice'];  
                $amka_cartella = dammi_cartella_articoli($amka_codice);               
                $esito = $pdo->exec("DELETE FROM articoli WHERE codice=$amka_codice");
                aggiorna_operazioni('articoli',$amka_codice,'Cancellazione',$amkf_descrizione);                
                cancella_cartella($amka_cartella, $amka_codice);
                $amks_eseguito = 'articolo ' . $amkf_descrizione . 'eliminato';
                require('proc_ritorno.php');
                exit;
            }                            
        }
    }
// ------------ preparazione form ------------------------------------------------------------------------------------    
    require('proc_testata.php');
    echo '<div class="funzioni">Articoli - ' . $amks_operazione . '</div>';
    genera_form($amks_azione);
    visualizza_errore();
    if ($_GET['fnz'] == 'vis'   or $_GET['fnz'] == 'del'  )  echo '<fieldset disabled>';
    echo '<div class="col-25"><label>Categoria</label> </div> <div class="col-75"> <select name="campo07">';
    foreach ($pdo->query("SELECT * FROM catart ORDER BY descrizione") as $r) {
        $amka_descrizione = $r['descrizione'];
        $amka_codice = $r['codice'];
        echo '<option value="'.$amka_codice.'" '; if ($amkf_categoria == $amka_codice) echo 'selected'; echo '>'.$amka_descrizione.'</option>';
    }
    echo ' </select> </div>  ';         
    genera_campo_grande('campo01', 'Descrizione', $amkf_descrizione, 'Descrizione articolo', 'autofocus');
    genera_campo('campo02', 'Unit&agrave; di misura', $amkf_unita_misura, 'Unit&agrave; di misura (kg, rotoli, litri ecc.)', '');
    genera_campo('campo03', 'Quantit&agrave; confezione', $amkf_qta_confezione, 'Quantit&agrave; presente in una confezione', '');    
    genera_campo('campo04', 'Prezzo', $amkf_prezzo, 'Prezzo per confezione', '');    
    genera_campo('campo05', 'Giacenza minima', $amkf_giacenza_minima, 'Giacenza minima)', '');    
    if ($_GET['fnz'] <> 'vis' and $_GET['fnz'] <> 'del')     
        genera_campo_barcode('campo06', 'Barcode', $amkf_barcode, 'Barcode, se non inserito sarà generato in automatico', '');    
    else
        genera_campo('campo06', 'Barcode', $amkf_barcode, 'Barcode, se non inserito sarà generato in automatico', '');    
    if ($_SESSION['app'] == 'S') genera_campo_note($amkf_note);        
    if($_GET['fnz'] == 'vis'    or $_GET['fnz'] == 'del'  ) echo '</fieldset>';
    visualizza_foto_e_immagini();
    visualizza_allegati();    
    if ($_GET['fnz'] == 'add' or $_GET['fnz'] == 'var') {
        echo ' <input type="submit" name="foto" value="Foto">';
        echo ' <input type="submit" name="immagine" value="Immagine">';        
        echo ' <input type="submit" name="allegato" value="Allegato">';
    }
    if ($_GET['fnz'] <> 'vis')   echo ' <input class="bottone_azione" type="submit" name="dati" value="' . $amks_bottone . '">';
    echo ' </form>';
    if ($_GET['fnz'] == 'vis'  and $_SESSION['app'] == 'S')   echo '<br><center><a href="operazioni_vis.php?tabella=articoli&amk=' .$_SESSION['amk'].'" class="bottone_menu">Storico operazioni</a>';    
    if ($_GET['fnz'] == 'vis') aggiorna_operazioni('articoli',$_SESSION['codice'],'Visualizzazione',$amkf_descrizione);                
    echo '</body> </html>';
}
catch (PDOException $e) { gestione_errori_try("Errore imprevisto riga " . $e->getLine ( ) . $e->getFile ( ) ." ".$e->getMessage());}