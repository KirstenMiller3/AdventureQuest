
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
			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			hintDiv.text(hintFromServer);
		},
	});
	
});

$('#hintform').click(function(e) {
	e.preventDefault();



	$.ajax({
		type: 'GET',
		url: '/adventureQuest/quest_ajax/',
		data: {click: true},
		success: function(response) {
			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			hintDiv.text(hintFromServer);
		},
	});

});

