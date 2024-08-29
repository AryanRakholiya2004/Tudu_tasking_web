
// Note form show | hide functions
function shownote()
{
    var list_length = $('#list_choice option').length;
    // alert(list_length);
    if(list_length < 3)
    {
        $('#list_choice_fld').hide();
        $('#new_list_form').removeClass('d-none');
    }
    document.getElementById('noteform').style.display = "block";
}
function hidenote()
{
    document.getElementById('noteform').style.display = "None";
}

// Add list functions
function showaddlist()
{
    document.getElementById('addlist').style.display = "flex";
}
function checklenght()
{
    var lg = document.getElementById('inputlist').value;
    if(lg.length >= 3)
    {
        document.getElementById('addlistbtn').style.backgroundColor = "green";
        $('#addlistbtn').attr('type', 'submit');
        $('input').on('keypress', function(event) {
            if (event.which === 13) {
                // Enter ajax code here...
            }
        });
    }
    else
    {document.getElementById('addlistbtn').style.backgroundColor = "black"; $('#addlistbtn').removeAttr('type', 'submit');}
}
function hideinputlist()
{
    document.getElementById('inputlist').value = '';
    document.getElementById('addlist').style.display = "None";
}

function iconanimation()
{
    $('#settings').toggleClass('rot-180');
}

// List tab
$('.task_list').click(function(){
    var taskList_id = $(this).attr('id');
    $('.task_list').removeClass('active_list');
    $('#' + taskList_id).addClass('active_list');
    $('.all-list').hide();
    $('.'+ taskList_id + '-list').show();
});

// Add list choice form
$('#list_choice').change(function(){
    var choice = $(this).val();
    // alert(choice);
    if(choice == 1)
    {
        $('#new_list_form').removeClass('d-none');
    }
    else
    {
        $('#new_list_form').addClass('d-none');
    }
});