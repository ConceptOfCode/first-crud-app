var btn = $('#getRes');
btn.click(function () {

    // $.ajax({
    //     type: 'GET',
    //     uri: 'test/getResponse'
    // }).done(function (result) {
    //     console.log(result.data);
    // })

    $.get('/test/getResponse', function (result) {
        console.log(result.data);
    });

});