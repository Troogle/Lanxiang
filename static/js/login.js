$(document).ready(function() {
    var $registerButton = $('#registerButton'),
        // default 0 is player, 1 is judger
        userType = 0,
        me = this;
    $("#registerButton").click(function() {
        var l = Ladda.create(this);
        l.start();
        l.setProgress(0.1);
        var $osuid = $('#osuid').val();
        var isPlayer = $('#player').prop('checked');
        me.userType = isPlayer? 0 : 1;
        console.log('userType:', me.userType );

        $registerButton.find('.ladda-label').text('请稍等');
        $.get('/register/getcode?id=' + $osuid + '&type=' + me.userType, function(response) {
            if (JSON.parse(response).code == -1) {
                alert('已经报名过或者id输入不正确，请刷新页面后重试');
                $registerButton.find('.ladda-label').text('报名失败');
                l.setProgress(1);
                l.stop();
                $registerButton.removeClass("btn-primary");
                $registerButton.addClass("btn-danger");
                $registerButton.attr("disabled", true);
            } else {
                l.setProgress(1);
                l.stop();
                $registerButton.find('.ladda-label').text('报名成功！');
                $registerButton.removeClass("btn-primary");
                $registerButton.addClass("btn-success");
                $registerButton.attr("disabled", true);
            }
        }).fail(function(response) {
            alert('网络连接中断。');
        });
    });
    $('#register').on('hidden.bs.modal', function(e) {
        $registerButton.find('.ladda-label').text('点击报名');
        $registerButton.attr("class", "btn btn-primary ladda-button");
        $registerButton.attr("disabled", false);
        $('#osuid').val("");
    })
});