$(function() {
  $('#pro').on('click', function() {
      window.location='https://immob.azurewebsites.net/professionel'
  });
})
$(function() {
  $('#par').on('click', function() {
      window.location='https://immob.azurewebsites.net/particulier'
  });
})
$(function() {
  $('#etp1').on('click', function() {
    $('#firstStep').hide();
    let tpb = $('#typBien').val();
    console.log(tpb);
    if (tpb == 1 || tpb ==2)
    {
      $('#SecondStep').show();
  
    }
    else{
      $('#SecondStepOption2').show();
    }
  });
})
$(function() {
  $('#etp2').on('click', function() {
    $('#firstStep').hide();
    $('#SecondStep').hide();
    $('#SecondStepOption2').hide();
    $('#StepThree').show();
  });
})
$(function() {
  $('#etp2-1').on('click', function() {
    $('#firstStep').hide();
    $('#SecondStep').hide();
    $('#SecondStepOption2').hide();
    $('#StepThree').show();
  });
})
$(function(){
  $('#etp3').on('click', function() { 
  let tpb = $('#typBien').val();
  let srb = $('#srb').val();
  let np = $('#np').val();
  let nd = $('#nd').val();
  let st = $('#srbm').val();
  let nt = 1
  let npt = 0
if(tpb == 1 || tpb == 2){
  tpbs = 'Seul'
  if(tpb == 1)
  {
    app =1
    loc =0
    mai =0
    ter =0
  }else{
    app =0
    loc =0
    mai =1
    ter =0
  }
$.getJSON('https://immob.azurewebsites.net/predict/'+ tpbs +'/' + srb +'/'+ np + '/' + st + '/'+ nd + '/' + app + '/' + loc + '/' + mai + '/' + ter , function(data) {        
  console.log(data)   
  for (var i = 0; i < data.length ; i++)
        {
          console.log(`${data[i][0]}`)
          var msg = `${data[i][0]}`
          $('#popup').show();
          $('#price').html(+msg+" €");
          setTimeout(function() {
            $('#gif_wait').hide();
        },5000)
}});
  }else{

  }
});
})
$(function() {
  $('#etap1').on('click', function() {
    $('#firstSteps').hide();
    let tpbien = $('#typDeBien').val();
    console.log(tpbien);
    if (tpbien == 1 || tpbien == 3)
    {
    $('#secondSteps').show();
    }
    else if(tpbien == 2 ){
      $('#secondSteps-2').show();
    }
    else
    {
      $('#secondSteps-3').show();
    }
  });
})
$('#close').on('click', function() {
  $('#popup').hide()
})

$('#etap3').on('click', function() {

  let srb = $('#srbati').val();
  let np = $('#npiece').val();
  let nd = $('#ndep').val();
  let st = $('#sutr').val();
let tpb = $('#typDeBien').val();
if(tpb == 1 || tpb == 3){
  if(tpb == 1)
  {
    tpbs = "Batiment"
    app = $('#nApp').val();
    loc =0
    mai =0
    ter =0
  }else{
    tpbs = "Lotissement"
    app =0
    loc =0
    mai =$('#nApp').val();
    ter =0
  }
$.getJSON('https://immob.azurewebsites.net/predict/'+ tpbs +'/' + srb +'/'+ np + '/' + st + '/'+ nd + '/' + app + '/' + loc + '/' + mai + '/' + ter, function(data) {        
  console.log(data)   
  for (var i = 0; i < data.length ; i++)
  {
    console.log(`${data[i][0]}`)
    var msg = `${data[i][0]}`
    $('#popup').show();
    $('#price').html(+msg+" €");
    setTimeout(function() {
      $('#gif_wait').hide();
  },5000)
        }});
  }

})


