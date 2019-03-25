var dataShow = {
    uploadFile: null, // 上传的文件
}; // 命名空间

$("#toUpload").fileinput({
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

$('#toUpload').on('fileloaded', function (event, file, previewId, index, reader) {  // 文件成功加载监听
    console.log(event);
    dataShow.uploadFile = file; // 文件对象实例
});

$('#toUpload').on('filecleared', function (event) {  // 清除按钮监听
    console.log("filecleared");
    dataShow.uploadFile = null;
});

$('#toUpload').on('fileselect', function (event, num) {  // 文件选择监听
    if (num == 0) {
        dataShow.uploadFile = null;
    }
});

setTimeout(function () {
    $($(".btn-frame").contents()[0].getElementsByClassName("btn-icon")).click(function () {
        ctrl($(this).attr("data"));
    })
}, 1000);

function ctrl(con){
    switch (con) {
            /*
             * 弹窗相关文档参阅：
             * http://www.runoob.com/bootstrap/bootstrap-modal-plugin.html
             * http://jschr.github.io/bootstrap-modal/
             */
            case '1':
                var modal1 = $("#Modal1");
                modal1.modal({ // 可以在这里通过remote属性添加HTML页面作为弹窗内容
                    backdrop: false
                })
                modal1.on('hide.bs.modal', function () {
                    alert('弹窗被关闭');
                })
                $('#SubmitModal1').click(function () {
                    alert('提交事件');
                })
                break;
            case '2':
                var modal2 = $("#Modal2");
                modal2.modal({
                    backdrop: false
                })
                $('#SubmitModal2').click(function () {
                    alert('提交事件');
                    console.log($("#form1").serialize())
                    modal2.modal('hide') // 关闭弹窗
                })
                break;
            case '3':
                if (dataShow.uploadFile == null) {
                    alert("未选择文件");
                } else {
                    alert("已选择文件")
                    console.log(dataShow.uploadFile)
                }
                break;
            case '4':
                break;
            case '5':
                break;
            case '6':
                break;
            case '7':
                break;
            case '8':
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
