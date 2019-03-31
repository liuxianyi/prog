var dataShow = {
    uploadFile: null, // 上传的文件
}; // 命名空间
var toUpload = $("#toUpload");
toUpload.fileinput({
    language: 'zh',
    allowedFileExtensions: ['txt', 'xlsx', 'xls'], // 接受的后缀
    maxFileCount: 1, //表示允许同时上传的最大文件个数
    showPreview: false, // 不显示拖拽区
    showUpload: false,
    removeIcon: '<i class="icon-remove"></i>',
    removeClass: 'btn btn-outline-danger my-2 my-sm-0',
    previewFileIcon: '<i class="icon-ok"></i>', // 文件图标
    browseClass: 'btn btn-outline-primary my-2 my-sm-0',
    // captionClass: 'dark-transp-bg text-light',
    // mainClass: 'dark-transp-bg text-light',
});

toUpload.on('fileloaded', function (event, file, previewId, index, reader) {  // 文件成功加载监听
    console.log(event);
    dataShow.uploadFile = file; // 文件对象实例
});

toUpload.on('filecleared', function (event) {  // 清除按钮监听
    console.log("filecleared");
    dataShow.uploadFile = null;
});

toUpload.on('fileselect', function (event, num) {  // 文件选择监听
    if (num == 0) {
        dataShow.uploadFile = null;
    }
});

setTimeout(function () {
    $($(".btn-frame").contents()[0].getElementsByClassName("btn-icon")).click(function () {
        ctrl($(this).attr("data"));
    })
}, 1000);

    /* 上传Form处理，modal弹窗对象、form表格对象、url接口、fSuccess成功回调函数、 fFail失败回调函数*/
    let uploadForm = function(modal, form, url, fSuccess, fFail){
        modal.click(function () {
            cookie = $.cookie("csrftoken");
            $.ajax({
                url: url,  // 算法1的接口
                data: form.serialize(),
                type: 'POST',
                async: true,
                headers:{"X-CSRFToken":cookie},
                success: function(res){
                    fSuccess(res);
                    },
                fail: function(res){
                    fFail(res);
                }
            })
        });
    };

function ctrl(con){

    let iframe = $('#showHtml');
    switch (con) {
            /*
             * 弹窗相关文档参阅：
             * http://www.runoob.com/bootstrap/bootstrap-modal-plugin.html
             * http://jschr.github.io/bootstrap-modal/
             */
            case '1':
                let modal1 = $("#Modal1");
                modal1.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                /*modal1.on('hide.bs.modal', function () {
                    alert('弹窗被关闭');
                });*/
                uploadForm($('#SubmitModal1'), $("#form1"), "/index/", function(res){
                    console.log(res.success);  // 成功回调函数
                        //iframe.attr("src", '/show_html1/'+src).then(resizeIframe);
                        console.log('更换show_html');
                        window.location.reload();
                        modal1.modal('hide') // 关闭弹窗
                    // if(res.success == 1){
                    //
                    // }else {
                    //     alert('please wait while!')
                    // }

                }, function(res){
                    console.error(res);  // 失败回调函数
                    // alert(res.error)
                });
                break;
            case '2':
                let modal2 = $("#Modal2");
                modal2.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal2'), $("#form2"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal2.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            case '3':
                /** 这个是文件操作，可以直接拼接到data中传入后端*/
                // if (dataShow.uploadFile == null) {
                //     alert("未选择文件");
                // } else {
                //     alert("已选择文件111111");
                //     console.log(dataShow.uploadFile)
                // }

                let modal3 = $("#Modal3");
                modal3.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal3'), $("#form3"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal3.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            case '4':
                let modal4 = $("#Modal4");
                modal4.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal4'), $("#form4"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal4.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            case '5':
                let modal5 = $("#Modal5");
                modal5.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal5'), $("#form5"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal5.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            case '6':
                let modal6 = $("#Modal6");
                modal6.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal6'), $("#form6"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal6.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            case '7':
                let modal7 = $("#Modal7");
                modal7.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal7'), $("#form7"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal7.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            case '8':
                let modal8 = $("#Modal8");
                modal8.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                });
                uploadForm($('#SubmitModal8'), $("#form8"), '/index/', function(res){
                    console.log(res.success);  // 成功回调函数
                    console.log('更换show_html');
                    window.location.reload();
                    modal8.modal('hide') // 关闭弹窗
                }, function(res){
                    console.error(res);  // 失败回调函数
                });
                break;
            default:
                console.log($(this).attr("data"))
        }
}
/*
var his = function () {
    let titleObj = $("#historyTitle");
    let showObj = [{
			"name": "标题1",
			"time": "2018.3.23",
            "info": "这个对象可以由JS动态替换"
		}, {
			"name": "标题2",
			"time": "2018.3.23"
		}, {
			"name": "标题3",
			"time": "2018.3.23",
			"info": "附加信息"
		}];
    titleObj.html("历史记录");
    $("#historyModalLabel").modal();
    let modalDiv = $("#historyModalDiv");
    modalDiv.html(''); // 清空原有内容
    let ul = $(`<ul class="list-group list-group-flush">`);
    for (key in showObj) {
        let ele=showObj[key];
            ul.append(`<li class="list-group-item`+(ele.info? (' cur-pointer" onclick="alert(\''+ele.info+'\')"') :'"')+`>`
                + ele.name + `<span class="float-right text-muted">` + ele.time + `</span></li>`)
    }
        if (!showObj.length) {
            ul.append(`<li class="list-group-item">Empty</li>`);
        }
    modalDiv.append(ul);
};*/
