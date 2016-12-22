$(document).ready(function(){
  $("#errorMsg").html('')
});

function resetSql() {
    $("#sql").val('');
}


function query() {
    var sql = $("#sql").val();
    if (!sql) {
        $("#errorMsg").html('查詢SQL不能为空！')
        return;
    }
    $("#doQuery").submit();
}