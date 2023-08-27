
add_custom_command(
    OUTPUT out.txt
    COMMAND sleep 5
    COMMAND echo "klaus" >| out.txt
  )

  add_custom_target(
    CustomCommand1
    DEPENDS out.txt
)
 