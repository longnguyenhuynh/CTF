<?php
    class Welcome
    {   
        public function __construct($name)
        {
            $this->name = $name;
        }


        public function invoke(){
            echo "Welcome {$this->name} to my world! <3";
        }

    }
?>