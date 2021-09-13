<?php
require_once('./welcome.class.php');
require_once('./signature.class.php');

class User 
{   
    public $welcome;

    public function __construct($name)
    {   
        $this->welcome = new Welcome($name);
        
    }

    public function __destruct()
    {
        $this->welcome->invoke();

    }
}
?>