function mashiroToc(mashiro) {
    // 滚动及悬浮
    $(document).ready(function() {
        if ($("div").hasClass("toc")) {
            var $elm = $('.toc');
            var iniTop = -1; 
            var finTop = 100; 
            if ($('.site-header').length){
                var hasScrolled = $('.site-header').offset().top;
            }
            if (hasScrolled > iniTop) {
                $elm.css({
                    'top': finTop
                });
            }
            $(window).scroll(function() {
                var p = $(window).scrollTop();
                if (p > iniTop - finTop) {
                    $elm.css({
                        'top': finTop
                    });
                } else {
                    $elm.css({
                        'top': iniTop - p
                    });
                }
            });
        }
    });
    // 初始化
    if (mashiro) {
        var id = 1;
        $(".entry-content").children("h2,h3,h4").each(function() {
            //var hyphenated = $(this).text().replace(/\s/g, '-');
            var hyphenated = "mashiro-" + id;
            $(this).attr('id', hyphenated);
            id++;
        });
        // 初始化 tocbot.js
        tocbot.init({
            headingsOffset: 60,
            tocSelector: '.toc',
            contentSelector: '.entry-content',
            headingSelector: 'h2, h3, h4',
            positionFixedSelector: ".toc",
            scrollEndCallback: function (e) {
                window.scrollTo(window.scrollX, window.scrollY);//如果加上了之后每次到一个新的结点就会卡
            },
        });
    }
}
mashiroToc(true);

