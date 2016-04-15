//点击删除选项
!function() {
    $("body").on('click', '.remove-box', function(e) {
	console.log("ok");
           var bbsId = $(e.target).data('bbsid');
	   $.get('/remove', {"bbs_id": bbsId}, function(data) {
   		if (data == 'OK') {
    		    $(e.target).parents('span').remove();
		}
	   })
    })  
}(this);

