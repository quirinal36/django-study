$(function(){
    // 페이지 로드 후 3초 후에 #sub-header 숨기기
    setTimeout(function(){
        $("#sub-header").hide();

        // 2초 후에 스크롤 방지 클래스를 제거
        $("html, body").removeClass("no-scroll");
    }, 2000);
});