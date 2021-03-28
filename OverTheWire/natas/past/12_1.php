<? 

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
}

// 만약 filename 이 있으면, filename의 값과 "upload"라는 키워드를 mrpf 함수에 넣는다.
// 그러면 입력된 filename 값의 경로 정보와 "upload"를 mrp 함수에 넣는다.
// 그러면 여기서는 "upload" 밑에 grs 함수 값/ filename 값의 경로. 순으로 경로를 만듦
// 10개의 무작위 숫자와 문자 배열을 만드는게 grs 함수다.

// 만약 업로드된 파일의 크기가 1000 보다 크면 파일이 너무 크다고 한다
// 
?>


