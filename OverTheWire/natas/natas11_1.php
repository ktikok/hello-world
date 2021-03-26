<?php

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
////////////////////////////////////////////////////////////////////////
// 우리는 저렇게 암호화된 문자열을 갖고 있음. 근데 그 암호화 된거는 no 값을 가짐. 
// 이걸 거꾸로 하면 암호화 되기전의 평문을 구할 수 있음. 그래서 암호화 된것을 거꾸로 저함수들에 집어넣어보자.
////////////////////////////////////////////////////////////////////////////////////

// 데이터^키 = 암호
// 암호^데이터 = 키

// $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);

function xor_encrypt_no() {
    //$key = '<censored>';
    // Cookie	data=ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D

    $cookie = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");
    print $cookie;
    echo "\n";

    $plain = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    
    print $plain;
    echo "\n";
    // load : 디코드 된 쿠키데이터임.
    // save : json_decode 된 어레이임 평문이 됨.
    $key = '';
    // Iterate through each character
    for($i=0;$i<strlen($plain);$i++) {
    //    echo $i;
    //    echo "\n";
    

    $key .= $plain[$i] ^ $cookie[$i % strlen($cookie)];
    // load : 이제 평문을 가짐
    // save : 평문이 알수 없는 글이 됨. 이제 base64로 디코드 되는 일만 남음. 
    }

    //우리가 아는 건 디코드 된 쿠키임. 그리고 그 쿠키는 no 값을 갖고 있음. 평문을 앎으로, 키를 구할 수 있음. 

    return $key;
}
//
//$defaultdata = c
//$jd = json_d
//xor_encrypt($defaultdata)

// echo xor_encrypt_no();

// output qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq

// encoded cookie^key = encoded array

// $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);


function xor_encrypt() {
    //$key = '<censored>';
    // Cookie	data=ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D
    $key = 'qw8J';

    $text = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
    print $text."\n";
    // load : 디코드 된 쿠키데이터임.
    // save : json_decode 된 어레이임 평문이 됨.
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        // print json_decode($outText) . "\n";
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    // load : 이제 평문을 가짐
    // save : 평문이 알수 없는 글이 됨. 이제 base64로 디코드 되는 일만 남음. 
    }

    //우리가 아는 건 디코드 된 쿠키임. 그리고 그 쿠키는 no 값을 갖고 있음. 평문을 앎으로, 키를 구할 수 있음. 

    return $outText;
}
$cookie = base64_encode(xor_encrypt());
print $cookie;
?>
