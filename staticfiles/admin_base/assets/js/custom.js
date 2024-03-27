
// const theButton = document.querySelector("#loginButton");

// theButton.addEventListener("click", () => {
//     theButton
// });


let majorBtn = document.querySelector('.major-btn');
let submitTextBtn = document.querySelector('.button-text');
let spinIconBtn = document.querySelector('.spin-icon');

let invalidUsername = document.querySelector('.invalid-username');
let emptyPassword = document.querySelector('.empty-password');
let invalidPassword = document.querySelector('.invalid-password');


function onPostLogin(event){
    event.preventDefault();
    
    let validate = ValidateForm();
    if(validate === true){
        majorBtn.setAttribute('disabled', 'disabled');
        submitTextBtn.setAttribute('hidden', 'hidden');
        spinIconBtn.removeAttribute('hidden');

    const loginButton = document.querySelector("#loginButton");
    loginButton.classList.add("button--loading");
    let username = $('#username').val();
    let password = $('#password').val();
    let csrf = jQuery("[name=csrfmiddlewaretoken]").val();

    let obj = {
        username: username,
        password: password,
        csrfmiddlewaretoken: csrf,
    }

    $.ajax({
        type: "POST",
        url: "/admin-user/",
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify(obj),
        success: function (result) {
            if (result.status){
                $(document.body).load(location.href);
                window.location.href = "/admin-user/dashboard/";

                majorBtn.removeAttribute('disabled');
                submitTextBtn.removeAttribute('hidden');
                spinIconBtn.setAttribute('hidden', 'hidden');
            }else{
                
            }
   
            },
            error: function (data) {
            console.log(data)
            majorBtn.removeAttribute('disabled');
            submitTextBtn.removeAttribute('hidden');
            spinIconBtn.setAttribute('hidden', 'hidden');
            alert("There was a problem while trying to Login");
            
            }
            
        });
    }else{
        return false
    }

    
}




function onApprove(event, id, index){
    event.preventDefault();

    Swal.fire({
        title: 'Are you sure you want to Approve this Transaction?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        ApproveButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        ApproveButtonText: 'Yes, Approve!'
      }).then((result) => {
        if (result.isConfirmed) {
            $('#cover-spin').show(0);
    

            $.ajax({
                type: "GET",
                url: `/admin-user/approved/${id}/`,
                success: function (result) {
                    if (result.Error){
                        $('#cover-spin').hide(0);
                        alert(result.Error);
                        Swal.fire(
                            'There was a problem while trying to Approve the Transaction!',
                            'Transaction Error.',
                            'error'
                          )
                    }else{
                        console.log(index)
                        $('#data-row-' + index).remove();
                        // $("tr[data-index='" + index +"']").remove();
                        $('#cover-spin').hide(0);
                        Swal.fire(
                            'Approved!',
                            'Transaction Approved.',
                            'success'
                          )
                    }
           
                    },
                    error: function (data) {
                    console.log(data);
                    alert("There was a problem  while trying to Login");
                    }
                });
        }
      })

 
}



function onApproveBooking(event, id, index){
    event.preventDefault();

    Swal.fire({
        title: 'Are you sure you want to Approve this Transaction?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        ApproveButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        ApproveButtonText: 'Yes, Approve!'
      }).then((result) => {
        if (result.isConfirmed) {
            $('#cover-spin').show(0);
    

            $.ajax({
                type: "GET",
                url: `/admin-user/booking/approved/${id}/`,
                success: function (result) {
                    if (result.Error){
                        $('#cover-spin').hide(0);
                        alert(result.Error);
                        Swal.fire(
                            'There was a problem while trying to Approve the Transaction!',
                            'Transaction Error.',
                            'error'
                          )
                    }else{
                        // $("tr[data-index='" + index +"']").remove();
                        $('#data-row-'+index).remove();
                        $('#cover-spin').hide(0);
                        Swal.fire(
                            'Approved!',
                            'Transaction Approved.',
                            'success'
                          )

                          
                        // $('#pendingListId').load('/authenticate/pending/partial');
                    }
           
                    },
                    error: function (data) {
                    console.log(data);
                    alert("There was a problem  while trying to Login");
                    }
                });
        }
      })

 
}



function onGetPendingTrainingTransactionDetails(event, id){
    event.preventDefault();
    
    $.ajax({
        type: "GET",
        url: `/admin-user/pending/${id}/`,
        success: function (result) {
            if (result.Error){
                $('#cover-spin').hide(0);
                alert(result.Error);
                Swal.fire(
                    'There was a problem while trying to get the Transaction!',
                    '',
                    'error'
                  )
            }else{                
                $('#detailsId').html(result)
                $('#viewId').modal("show")
            }
   
            },
            error: function (data) {
            console.log(data);
            alert("There was a problem  while trying to Get the Data");
            }
        });
}



function onGetPendingBookingTransactionDetails(event, id){
    event.preventDefault();
    
    $.ajax({
        type: "GET",
        url: `/admin-user/booking/pending/${id}/`,
        success: function (result) {
            if (result.Error){
                $('#cover-spin').hide(0);
                alert(result.Error);
                Swal.fire(
                    'There was a problem while trying to get the Transaction!',
                    '',
                    'error'
                  )
            }else{                
                $('#detailsId').html(result)
                $('#viewId').modal("show")
            }
   
            },
            error: function (data) {
            console.log(data);
            alert("There was a problem  while trying to Get the Data");
            }
        });
}



function onGetApprovedTrainingTransactionDetails(event, id){
    event.preventDefault();
    
    $.ajax({
        type: "GET",
        url: `/admin-user/approved/get/${id}/`,
        success: function (result) {
            if (result.Error){
                $('#cover-spin').hide(0);
                alert(result.Error);
                Swal.fire(
                    'There was a problem while trying to get the Transaction!',
                    'Transaction Error.',
                    'error'
                  )
            }else{                
                $('#approved-detailsId').html(result)
                $('#approvedId').modal("show")
            }
   
            },
            error: function (data) {
            console.log(data);
            alert("There was a problem  while trying to Get the Data");
            }
        });
}



function onGetApprovedBookingTransactionDetails(event, id){
    event.preventDefault();
    
    $.ajax({
        type: "GET",
        url: `/admin-user/booking/approved/get/${id}/`,
        success: function (result) {
            if (result.Error){
                $('#cover-spin').hide(0);
                alert(result.Error);
                Swal.fire(
                    'There was a problem while trying to get the Transaction!',
                    'Transaction Error.',
                    'error'
                  )
            }else{                
                $('#approved-detailsId').html(result)
                $('#approvedId').modal("show")
            }
   
            },
            error: function (data) {
            console.log(data);
            alert("There was a problem  while trying to Get the Data");
            }
        });
}


function onCloseModal(id){
    $(`#${id}`).modal('hide');
}



// The Validation Functions
function ValidateEmail()  
{  
var x=document.myform.email.value;  
var atposition=x.indexOf("@");  
var dotposition=x.lastIndexOf(".");  
if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length){  
  alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
  return false;  
  }  
}



function ValidateForm(){  
    var username=document.myform.username.value;  
    var password=document.myform.password.value;  
      
    if(username == "" && password == ""){
        invalidUsername.removeAttribute('hidden');
        emptyPassword.removeAttribute('hidden');
        return false
    }else if(username == "" && password !== ""){
        emptyPassword.setAttribute('hidden', 'hidden');
        invalidPassword.setAttribute('hidden', 'hidden');
        invalidUsername.removeAttribute('hidden');
        return false
    }else if(username !== "" && password == ""){
        invalidUsername.setAttribute('hidden', 'hidden');
        invalidPassword.setAttribute('hidden', 'hidden');
        emptyPassword.removeAttribute('hidden'); 
        return false
    }else if(username !== "" && password.length < 5){
        invalidUsername.setAttribute('hidden', 'hidden');
        emptyPassword.setAttribute('hidden', 'hidden');
        invalidPassword.removeAttribute('hidden'); 
    }else if(username == "" && password.length < 5){
        emptyPassword.setAttribute('hidden', 'hidden');
        invalidUsername.removeAttribute('hidden');
        invalidPassword.removeAttribute('hidden'); 
    }else{
        return true;
    }

  
    }  