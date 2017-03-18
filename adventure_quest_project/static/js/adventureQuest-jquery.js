
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

			var available = response['hint_available'];

			console.log('woooooooooooooooooooooooooo', available);

			if (available === 'false'){
				var button = $('#hintform')
					button.hide();
				console.log('testing if', available);
			}
			else if (available === 'true'){
				var button = $('#hintform')
					button.show();
				console.log('testing if', available);
			}

		},
	});
	
});

$('#hintform').click(function(e) {
	$('#hintform').click('disabled', false)
	e.preventDefault();

	$.ajax({
		type: 'GET',
		url: '/adventureQuest/quest_ajax/',
		data: {click: true},
		success: function(response) {
			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			hintDiv.text(hintFromServer);

			var hintNoDiv = $('#hintNo');
			var x = response['hintNo'];
			hintNoDiv.text(x);

			var available = response['hint_available'];

			console.log('woooooooooooooooooooooooooo', available);
			if (available === 'false'){
				var button = $('#hintform')
					button.hide();
				console.log('testing if', available);
			}
			else if (available === 'true'){
				var button = $('#hintform')
					button.show();
				console.log('testing if', available);
			}




		},
	});

});

