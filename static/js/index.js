$(document).ready(function() {
    $_zhihu = $('#wrapper .zhihu')
    $_juejin = $('#wrapper .juejin')
    $_zhTpl = $('#wrapper .zh-tpl')
    $_jjTpl = $('#wrapper .jj-tpl')

    $_juejin.on('click', function() {
        $_juejin.addClass('active')
        $_zhihu.removeClass('active')
        $_jjTpl.addClass('show')
        $_zhTpl.removeClass('show')
    })

    $_zhihu.on('click', function() {
        $_zhihu.addClass('active')
        $_juejin.removeClass('active')
        $_zhTpl.addClass('show')
        $_jjTpl.removeClass('show')
    })
})