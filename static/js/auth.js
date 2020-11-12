const validate = () => {
    let form = document.forms["authForm"]

    if (form['email'].value == "" || form['code'].value == "") {
        alert('Fill out the form correctly!')
        return false
    }
    return true
}