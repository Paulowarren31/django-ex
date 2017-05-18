$(function(){
  accounts = $('[id^=acc]').not('[id$=cat]').not('[id$=i]')
  accounts.on('click', function(e){
    acc_pk = e.target.parentNode.id.split('-')[1]

    categories = $('[id^=acc-'+acc_pk+'][id$=cat]').toggleClass('hidden')
    //get all categories
  })

  categories = $('[id^=acc][id$=cat]')
  console.log(categories)

  categories.on('click', function(e){
    acc_pk = e.target.parentNode.id.split('-')[1]
    cat_pk = e.target.parentNode.id.split('-')[3]

    items = $('[id^=acc-'+acc_pk+'-cat-'+cat_pk+']').not('[id$=cat]').toggleClass('hidden')
    console.log(items)
  })

})
