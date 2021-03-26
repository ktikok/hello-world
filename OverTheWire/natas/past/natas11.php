<?


function xor_encrypt($in) {
    //$key = '<censored>';
    // Cookie	data=ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D
    $key = '<censored>';

    $text = $in;
    // load : 디코드 된 쿠키데이터임.
    // save : json_decode 된 어레이임 평문이 됨.
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    // load : 이제 평문을 가짐
    // save : 평문이 알수 없는 글이 됨. 이제 base64로 디코드 되는 일만 남음. 
    }

    //우리가 아는 건 디코드 된 쿠키임. 그리고 그 쿠키는 no 값을 갖고 있음. 평문을 앎으로, 키를 구할 수 있음. 

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    //echo $_COOKIE;
    print_r($_COOKIE);
    
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
////////////////////////////////////////////////////////////////////////
// 이걸 거꾸로 하면 암호화 되기전의 평문을 구할 수 있음. 그래서 암호화 된것을 거꾸로 저함수들에 집어넣어보자.
////////////////////////////////////////////////////////////////////////////////////

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
//echo $defaultdata;

// cookie
    // load base64 보호된 쿠키
        //xor 보호된 쿠키^key = 보호 해지된 쿠키
            // json 보호 해제된 쿠키
                // 보호 해제된 정보 읽기 여기서 showpassword ==yes여야함. 
            // save json 보호 해제된 쿠키
        // xor a^key^key 다시 보호
    // base64 a > current cookie and other values.



//echo json_encode($defaultdata);
// Fatal error: Uncaught Error: Call to undefined function json_encode()
print_r($defaultdata);
$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);


?>

<?
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}

?>