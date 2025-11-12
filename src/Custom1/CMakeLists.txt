

add_custom_command(
  OUTPUT 
    ${CMAKE_CURRENT_SOURCE_DIR}/out
    ${CMAKE_CURRENT_SOURCE_DIR}/out/out1.txt
    ${CMAKE_CURRENT_SOURCE_DIR}/out/out2.txt
  COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_CURRENT_SOURCE_DIR}/out
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_CURRENT_SOURCE_DIR}/out
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_CURRENT_SOURCE_DIR}/out/out1.txt
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_CURRENT_SOURCE_DIR}/out/out2.txt
  COMMENT "Generating out"
)

add_custom_target(
  CustomCommand1
  DEPENDS 
    ${CMAKE_CURRENT_SOURCE_DIR}/out
    ${CMAKE_CURRENT_SOURCE_DIR}/out/out1.txt
    ${CMAKE_CURRENT_SOURCE_DIR}/out/out2.txt
)
 