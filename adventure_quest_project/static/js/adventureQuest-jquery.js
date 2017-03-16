
/* Ajax Query */

$('#questionform').submit(function(e) {
	e.preventDefault();
	
	var questionBox = $('#question');
	var answerValue = questionBox[0].value;
	
	$.ajax({
		type: 'GET',
		url: '/adventureQuest/quest_ajax/',
		data: {'answer': answerValue},
		success: function(response) {
			var answerDiv = $('#answer');
			var answerFromServer = response['answer'];
			
			answerDiv.text(answerFromServer);
			questionBox.val('');
		},
	});
	
});

