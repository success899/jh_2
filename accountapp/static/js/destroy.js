function initialize(pk) {
    axios.get('/accounts/retrieve/' + pk )
        .then(function (response) {
            // handle success
            console.log(response);

            document.getElementById('username').value = response.data['username'];
            document.getElementById('email').value = response.data['email'];

        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });
}

function delete_account(pk) {
    axios.delete('/accounts/delete/' + pk)
        .then(function (response) {
            // handle success
            console.log(response);

            window.location.href = '/accounts/hello_world_template/';
        })
        .catch(function (error) {
            // handle error
            console.log(error);

            document.getElementById('alert_box').innerHTML
                    = "<div class='btn btn-danger rounded-pill px-5'>탈퇴에 실패했습니다.</div>"
        })
        .then(function () {
            // always executed
        });
}