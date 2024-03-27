
function triggerSubmitIcon(){
  $("#serviceSubmitBtn").attr("disabled", "disabled")
  $("#submitServicesTextId").attr("hidden", "hidden")
  $("#serviceLoadingIconId").removeAttr("hidden")
}

function disableTriggerSubmitIcon(){
  $("#serviceSubmitBtn").removeAttr("disabled")
  $("#submitServicesTextId").removeAttr("hidden")
  $("#serviceLoadingIconId").attr("hidden", "hidden")
  $("#sText").attr("hidden", "hidden")
}


function onPostServiceBooking(event){
    event.preventDefault();
    
    triggerSubmitIcon()

    let amount = $('#amountId').val().replaceAll(",", "")
    amount = amount.substring(1)
    
    var formData = new FormData();
    formData.append('serviceId', $('#serviceId').val());
    formData.append('durationId', $('#durationId').val());
    formData.append('preferedDateId', $('#preferedDateId').val());
    formData.append('amountId', amount);
    formData.append('accountId', $('#accountId').val());
    formData.append('paymentProofId', $('#paymentProofId')[0].files[0]);
    formData.append('csrfmiddlewaretoken', jQuery("[name=csrfmiddlewaretoken]").val());
        
      $.ajax({
      type: "POST",
      url: "/services-payment/post",
      processData: false,
      contentType: false,
      mimeType: "multipart/form-data",
      data: formData,
      success: function (result) {        
      $("#paymentProofId").val("")
      $("#preferedDateId").val("")

      $("#serviceSubmitBtn").removeAttr("disabled")
      $("#submitServicesTextId").removeAttr("hidden")
      $("#serviceLoadingIconId").attr("hidden", "hidden")
      $("#sText").attr("hidden", "hidden")

        //disableTriggerSubmitIcon()
        result = JSON.parse(result)        
        result.message && swal(`${result.title}!`, `${result.message}!`, `${result.status}`)
    
      },
          error: function (err) {
            disableTriggerSubmitIcon()
            console.log(err)
          }
      });
    
      }
    