#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: struct of type PyObject
 *
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t sz = PyList_Size(p), i;
	PyObject *it;

	printf("[*] Size of the Python List = %zd\n", sz);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < sz; i++)
	{
		it = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(it)->tp_name);
	}
}
