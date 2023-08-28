

IF(CMAKE_SYSTEM_NAME STREQUAL "Linux")
  add_custom_command(
      OUTPUT out.txt
      COMMAND sleep 5
      COMMAND echo "klaus" >| out.txt
    )
elseif(CMAKE_SYSTEM_NAME STREQUAL "Windows")
  add_custom_command(
    OUTPUT out.txt
    COMMAND ping -n 5 127.0.0.1
    COMMAND echo "klaus">out.txt
  )
endif()

  add_custom_target(
    CustomCommand1
    DEPENDS out.txt
)
 