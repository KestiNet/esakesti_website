<><script src="https://code.jquery.com/jquery-3.6.0.min.js"></script><script>
    $(document).ready(function() {$('#gonogoForm').submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: '/gonogo',
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log("Response received:", response);
                if (response.error) {
                    $('#result').text("Error: " + response.error);
                } else if (response.message) {
                    $('#result').html(response.message.replace(/\n/g, '<br>'));
                } else {
                    $('#result').text("Calculation complete, but no message received.");
                }
                $('#result').show(); // Ensure the result div is visible
            },
            error: function (xhr, status, error) {
                console.log("Error details:", { xhr: xhr, status: status, error: error });
                $('#result').text("An error occurred. Please try again.");
                $('#result').show();
            }
        });
    })};
    });
</script></>