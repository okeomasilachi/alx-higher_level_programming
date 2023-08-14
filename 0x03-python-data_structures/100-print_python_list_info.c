#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: struct of type PyObject
 *
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i;
	PyObject *item;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
