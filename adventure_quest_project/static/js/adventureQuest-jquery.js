
/* Ajax Riddle Submit Query */
$('#questionform').submit(function(e) {

	// Prevent form submission
	e.preventDefault();

	// Create question box and value
	var questionBox = $('#question');
	var answerValue = questionBox[0].value;

	// Set up ajax request
	$.ajax({
		type: 'GET',
		url: '/adventureQuest/quest_ajax/',
		data: {'answer': answerValue},
		success: function(response) {

			var answerDiv = $('#answer');
			var answerFromServer = response['answer'];

			// Update question and clear answer
			answerDiv.text(answerFromServer);
			questionBox.val('');

			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			//Update hint text
			hintDiv.text(hintFromServer);

			var instNoDiv = $('#instruction');
			var y = response['instruction'];
			// Update instruction text
			instNoDiv.text(y);

			var available = response['hint_available'];
			// Check if a hint is available and if not hide the hint button
			if (available === 'false'){
				var button = $('#hintform')
					button.hide();
			}
			else if (available === 'true'){
				var button = $('#hintform')
					button.show();
			}

			var lastQ = response['noRiddles']
			var currentQ = response['currentQ']
			var end = response['correct']
			// Check if the question is the last one and it was correct. If so
			// then redirect the user to the last page
			if(currentQ === lastQ-1 && end)
			{
				$(this).unbind('submit').submit()
				window.location = '../congratulations/'
			}

		},
	});
	
});

/* Ajax Hint Submit Query */
$('#hintform').click(function(e) {

	// Prevent form submission
	e.preventDefault();

	// Set up ajax request
	$.ajax({
		type: 'GET',
		url: '/adventureQuest/quest_ajax/',
		data: {click: true},
		success: function(response) {

			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			// Update the hint text
			hintDiv.text(hintFromServer);

			var hintNoDiv = $('#hintNo');
			var x = response['hintNo'];
			hintNoDiv.text(x);


			var available = response['hint_available'];
			console.log("hint it from click" + available)
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


