'use strict';
// 跨域问题的处理
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = Zepto.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// var csrftoken = getCookie('csrftoken');

function ConvertEmoji() {
    $(".convert-emoji").each(function() {
        var original = $(this).html();
        var converted = emojione.toImage(original);
        $(this).html(converted);
    });
}
/**
function init_emoji() {
    $(".my-emojionearea").emojioneArea({
        search: false,
        recent: false,
        recentEmojis: false,
        pickerPosition: "top",
        buttonTitle: "您可以使用TAB键快速插入表情",
        placeholder:"请输入您的评论",
        shortnames: true,
        tones: false,
        autocomplete: false,
        filters: {
            recent : false, // disable recent
            objects: false, // disable objects filter
            symbols: false, // disable symbols filter
            flags : false, // disable flags filter
            travel_places: false,
            animals_nature: false
        }
    });
}
 **/
function mobile_user_reply() {
    $(".send").click(function () {
  //console.log($(this).attr('.my-emojionearea').data("my-emojionearea").getText())
  var user_comment = $(".login").val();
  if (login){
     $.ajax(
        {
            type: 'POST',
            url: '/mobile/user/reply/',
            data: {"user_comment": user_comment, "article_id": mobile_article_id, "csrfmiddlewaretoken": csrftoken},
            dataType: "html",
            success: function (data) {
               if($(data).find("div").length > 0){
                   $('.comments').prepend(data);
                   ConvertEmoji();
                   $(".login").val('');
               }else {
                   console.log("=====")
               }
            }
        }
    );
  }else {
       swal({
                title: "您还没有登录",
                text: "请登录后为您喜爱的文章进行评价和点赞！",
                type: "warning",
                confirmButtonText: "确定"
            },function (isConfirm) {
                if(isConfirm){
                location.href="/accounts/login" + "?next=" + window.location.pathname;
            }
        });
  }

});
}
