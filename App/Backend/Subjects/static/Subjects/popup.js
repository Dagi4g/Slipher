function showPopup(subjectName) {
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');
    const nameElement = document.getElementById('subtopic-name');
    
    if (subjectName) {  // This checks for null, undefined, and empty strings
        nameElement.textContent = subjectName;
        popup.style.display = 'block';
        overlay.style.display = 'block';
    } else {
        popup.style.display = 'none';
        overlay.style.display = 'none';
    }
}

function closePopup() {
	document.getElementById('popup').style.display = 'none';

	document.getElementById('overlay').style.display = 'none';
}

function remembered() {
    closePopup();

    const subtopicName = document.getElementById('subtopic-name').textContent;

    fetch('/remembered/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
	    'Cache-Control': 'no-cache',
            'X-CSRFToken': getCookie('csrftoken')  // essential for Django .
        },
        body: JSON.stringify({ subtopic: subtopicName })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response:', data);
    })
    .catch(error => {
        console.error('Error sending subtopic:', error);
    });
}

// Helper function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        for (const cookie of document.cookie.split(';')) {
            const trimmed = cookie.trim();
            if (trimmed.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(trimmed.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function forgot() {
    closePopup();

    const subtopicName = document.getElementById('subtopic-name').textContent;

    fetch('/forgot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
	    'Cache-Control': 'no-cache',
            'X-CSRFToken': getCookie('csrftoken')  // essential for Django .
        },
        body: JSON.stringify({ subtopic: subtopicName })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response:', data);
    })
    .catch(error => {
        console.error('Error sending subtopic:', error);
    });
}



document.addEventListener('DOMContentLoaded', function() {
	fetch('/should_review/')
		.then(response => {
			if (!response.ok) throw new Error('Network error');
			return response.json();
		})
		.then(data => {

			if (data.should_review && data.subtopics.length > 0) {
				showPopup(data.subtopics[0].subtopic);
				
			}
		})
		.catch(error => {
			console.error('Error:', error);
                    // Optional: Show popup with generic message if API fails
                    // showPopup('your recent topics');

		});

});
