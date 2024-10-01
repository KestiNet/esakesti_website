$(document).ready(function() {
    // GoNoGo form submission
    $('#gonogoForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/gonogo',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                console.log("Server response:", response); // Add this line for debugging
                if (response.error) {
                    $('#result').text(response.error);
                } else {
                    $('#result').html(response.message.replace(/\n/g, '<br>'));
                }
            },
            error: function(xhr, status, error) {
                console.log("Error: " + error);
                console.log("Response Text: " + xhr.responseText);
                $('#result').text("An error occurred: " + error + ". Status: " + status);
            }
        });
    });

    // CTA button click event
    $('.cta').on('click', function(e) {
        e.preventDefault();
        alert('More information coming soon!');
    });

    // Dropdown button click event
    $('.dropbtn').on('click', function(e) {
        e.preventDefault();
        $(this).next('.dropdown-content').toggle();
    });
});