
function showPopup(subjectName) {
        const subjectElement = document.getElementById('subtopic-name');
        subjectElement.textContent = subjectName || 'this topic'; // Fallback if empty
        document.getElementById('popup').style.display = 'block';
        document.getElementById('overlay').style.display = 'block';
}

function closePopup() {
	document.getElementById('popup').style.display = 'none';

	document.getElementById('overlay').style.display = 'none';
}

function remembered() {
	closePopup();
	// Optional: Send to server that user remembers
	fetch('/remembered/', {
        method: 'POST',
        headers: {
		'Content-Type': 'application/json',
		'X-CSRFToken': '{{ csrf_token }}'
	}
	});
}

function forgot() {
	closePopup();
	window.location.href = '/review/'; // Update with your actual review URL
        }


document.addEventListener('DOMContentLoaded', function() {
	fetch('/should_review/')
		.then(response => {
			if (!response.ok) throw new Error('Network error');
			return response.json();
		})
		.then(data => {
			if (data.should_review) {
				// Check multiple possible locations for the subtopic name
				showPopup(data.subtopics.subtopic);
			}
		})
		.catch(error => {
			console.error('Error:', error);
                    // Optional: Show popup with generic message if API fails
                    // showPopup('your recent topics');

		});

});
