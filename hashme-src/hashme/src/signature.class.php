<?php
    include("secret.php");#contain $flag and $secret

    class Signature
    {   
        
        public function __construct($name)
        {
            $this->user = $name;
        }


        public function invoke(){
            global $secret;
            if ($this->name === "admin") {
                echo "Signature of admin is a secret <3. A secret makes a woman woman.<br>";
            } else {
                $sig = md5($secret.$this->name);
                echo "LOL, $this->name's signature: $sig <br>";
            }
        }

    }
    