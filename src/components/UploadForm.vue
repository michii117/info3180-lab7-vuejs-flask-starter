<template>
    <form action="" method="post" id="uploadForm"  @submit.prevent="uploadPhoto" >
        <label for="" id="textLabel">Description</label>
        <input type="text" name="" id="description">

        <label for="" id="photoLabel">Photo Upload</label>
        <input type="file" name="" id="photo">
        <input id="submit" type="submit" value="Submit">
    </form>
</template>


<script>
export default {
        data() {
            return {
                csrf_token: ''
            }
        },
        created() {
            this.getCsrfToken();
        },

        methods: {
            uploadPhoto() {
                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm);

                fetch("/api/upload", {
                    method: 'POST',
                    body: form_data,
                    headers: {
                        'X-CSRFToken': this.csrf_token
                    }
                })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (data) {
                        // display a success message
                        console.log(data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },
            getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                    .then((response) => response.json())
                    .then((data) => {
                        console.log(data);
                        self.csrf_token = data.csrf_token;
                    })
            }
        }
    }

</script>


<style>

label#textLabel, label#photoLabel {
    display: block;
    margin: 20px 0px;
    font-weight: 500;
}

form {
    margin: 0px 10%;
}

input#description {
    width: 90%;
    height: 50px;
    border: none;
    filter: drop-shadow(2px 2px 3px #00000055);
    border-radius: 5px;
    padding: 3px;
    font-size: 14px;
}

#submit {
    display:block;
    border: none;
    padding: 10px 20px;
    filter: drop-shadow(2px 4px 3px #00000044);
    background-color: #41b883;
    color: white;
    margin: 20px 0px;
}

</style>