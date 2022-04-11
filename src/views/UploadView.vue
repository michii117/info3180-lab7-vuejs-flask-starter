<script>
    import UploadForm from "@/components/UploadForm.vue";
   export default {
    data() {
        return {
            message: "Upload Form"
        };
    },
    components: { UploadForm }
}
    
</script>


<template>
    <div class="upload-container">
        <h1> {{ message }} </h1>
        <UploadForm />
    </div>
</template>

<style>
h1{
    margin: 5% 10%;
}
</style>
