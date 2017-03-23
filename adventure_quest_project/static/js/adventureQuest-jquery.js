
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

		// Update question and clear answer
			var answerDiv = $('#answer');
			var answerFromServer = response['answer'];
			answerDiv.text(answerFromServer);
			questionBox.val('');

		// Update hint text
			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			hintDiv.text(hintFromServer);

		// Update instruction text
			var instNoDiv = $('#instruction');
			var y = response['instruction'];
			instNoDiv.text(y);

		// Check if a hint is available and if not hide the hint button
				var available = response['hint_available'];
			if (available === 'false'){
				var button = $('#hintform')
					button.hide();
			}
			else if (available === 'true'){
				var button = $('#hintform')
					button.show();
			}

		// Check if the question is the last one and it was correct. If so
		// then redirect the user to the last page
			var lastQ = response['noRiddles']
			var currentQ = response['currentQ']
			var end = response['correct']
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

		// Update the hint text
			var hintDiv = $('#hint');
			var hintFromServer = response['hint'];
			hintDiv.text(hintFromServer);

		// Update the number of hints displayed
			var hintNoDiv = $('#hintNo');
			var x = response['hintNo'];
			hintNoDiv.text(x);

		// Check if hint is available and then either show or hide the hint button
			var available = response['hint_available'];
			if (available === 'false'){
				var button = $('#hintform')
					button.hide();
			}
			else if (available === 'true'){
				var button = $('#hintform')
					button.show();
			}
		},
	});
});


