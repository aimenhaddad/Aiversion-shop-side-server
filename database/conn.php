<?php
$dbname="skycode_shop";
$servername = "localhost";
$username = "root";
$password = "";
      
try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
  die("Connection failed: " .$e->getMessage());
}

include_once 'produit.php';

$produit = new Produits($conn); 
?>