function submitAfterValidation() {
  var invalid = false;
  if ((Number(document.formation.num_of_FW.value) + Number(document.formation.num_of_MF.value) + Number(document.formation.num_of_DF.value))!= 10) {
        alert("palayerの合計が11になるように設定してください。");
        return;
  }
  document.formation.submit();
}