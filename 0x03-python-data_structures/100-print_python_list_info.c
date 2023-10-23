#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @list_obj: A PyObject list.
 */
void print_python_list_info(PyObject *list_obj)
{
    int list_size, list_alloc, i;
    PyObject *item_obj;

    list_size = Py_SIZE(list_obj);
    list_alloc = ((PyListObject *)list_obj)->allocated;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", list_alloc);

    for (i = 0; i < list_size; i++)
    {
        printf("Element %d: ", i);

        item_obj = PyList_GetItem(list_obj, i);
        printf("%s\n", Py_TYPE(item_obj)->tp_name);
    }
}
