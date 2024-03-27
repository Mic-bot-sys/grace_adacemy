
function triggerSubmitIcon(){
  $("#trainingSubmitBtn").attr("disabled", "disabled")
  $("#submitTextId").attr("hidden", "hidden")
  $("#loadingIconId").removeAttr("hidden")
}

function disableTriggerSubmitIcon(){
  $("#trainingSubmitBtn").removeAttr("disabled")
  $("#submitTextId").removeAttr("hidden")
  $("#loadingIconId").attr("hidden", "hidden")
}


function onPostTrainingEnrollment(event){
    event.preventDefault();
    
    triggerSubmitIcon()
    
    var formData = new FormData();
    formData.append('courseId', $('#courseId').val());
    formData.append('amount', $('#amount').val());
    // formData.append('paymentProof', $('#paymentProof').val());
    formData.append('accountId', $('#accountId').val());
    formData.append('paymentProof', $('#paymentProof')[0].files[0]);
    formData.append('csrfmiddlewaretoken', jQuery("[name=csrfmiddlewaretoken]").val());
        
      $.ajax({
      type: "POST",
      url: "/trainings-payment/post",
      processData: false,
      contentType: false,
      mimeType: "multipart/form-data",
      data: formData,
      success: function (result) {        
      $("#paymentProof").val("")
      disableTriggerSubmitIcon()
        result = JSON.parse(result)        
        result.message && swal(`${result.title}!`, `${result.message}!`, `${result.status}`)
    
      },
          error: function (err) {
            console.log(err)
          }
      });
    
      }
    