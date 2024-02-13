$(function(){
    // 맨 위로 스크롤 이동
    $("html, body").scrollTop(0);

    // #header button 클릭 시 동작
    $("#header button").click(function(){
        $("#header").hide();
        $("html, body").removeClass("no-scroll");
    });
});

// 페이지 주소 복사 함수
function copyPageURL() {
    // 현재 페이지 주소 가져오기
    const currentPageURL = window.location.href;

    // 가상의 textarea 엘리먼트를 생성하여 값을 복사하고 제거
    const textarea = document.createElement('textarea');
    textarea.value = currentPageURL;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    // 복사 성공 메시지 등 추가 가능
    alert('페이지 주소가 복사되었습니다.');
}

